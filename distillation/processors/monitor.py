"""Pipeline monitoring and observability utilities."""

import logging
import threading
import time
from dataclasses import dataclass
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False


@dataclass
class SystemMetrics:
    """Real-time system metrics."""

    timestamp: float
    cpu_percent: float
    memory_mb: float
    memory_percent: float
    disk_usage_percent: float
    network_connections: int


@dataclass
class PipelineEvent:
    """Pipeline execution event."""

    timestamp: float
    event_type: str
    phase: str
    message: str
    metadata: Dict[str, Any]


class PipelineMonitor:
    """Real-time monitoring for distillation pipeline execution."""

    def __init__(self, log_file: Optional[str] = None):
        """Initialize pipeline monitor."""
        self.logger = logging.getLogger(__name__)
        self.log_file = log_file
        self.events: List[PipelineEvent] = []
        self.system_metrics: List[SystemMetrics] = []
        self.monitoring_active = False
        self.monitor_thread: Optional[threading.Thread] = None

        # Performance thresholds
        self.memory_threshold_mb = 100.0
        self.cpu_threshold_percent = 80.0

        # Callbacks for alerts
        self.alert_callbacks: List[Callable[[str, Dict[str, Any]], None]] = []

    def start_monitoring(self, interval_seconds: float = 5.0):
        """Start real-time monitoring."""
        if self.monitoring_active:
            return

        self.monitoring_active = True
        self.monitor_thread = threading.Thread(
            target=self._monitoring_loop,
            args=(interval_seconds,),
            daemon=True
        )
        self.monitor_thread.start()
        self.logger.info("Pipeline monitoring started")

    def stop_monitoring(self):
        """Stop real-time monitoring."""
        self.monitoring_active = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=1.0)
        self.logger.info("Pipeline monitoring stopped")

    def log_event(self, event_type: str, phase: str, message: str, **metadata):
        """Log a pipeline event."""
        event = PipelineEvent(
            timestamp=time.time(),
            event_type=event_type,
            phase=phase,
            message=message,
            metadata=metadata
        )

        self.events.append(event)

        # Log to file if configured
        if self.log_file:
            self._write_event_to_file(event)

        # Check for alerts
        self._check_alerts(event)

        self.logger.info(f"[{phase}] {event_type}: {message}")

    def add_alert_callback(self, callback: Callable[[str, Dict[str, Any]], None]):
        """Add callback for alert notifications."""
        self.alert_callbacks.append(callback)

    def get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary from collected metrics."""
        if not self.system_metrics:
            return {"error": "No metrics collected"}

        # Calculate averages
        cpu_avg = sum(m.cpu_percent for m in self.system_metrics) / len(self.system_metrics)
        memory_avg = sum(m.memory_mb for m in self.system_metrics) / len(self.system_metrics)
        memory_percent_avg = sum(m.memory_percent for m in self.system_metrics) / len(self.system_metrics)

        # Find peaks
        cpu_peak = max(m.cpu_percent for m in self.system_metrics)
        memory_peak = max(m.memory_mb for m in self.system_metrics)

        # Calculate event statistics
        event_counts = {}
        for event in self.events:
            event_counts[event.event_type] = event_counts.get(event.event_type, 0) + 1

        phase_counts = {}
        for event in self.events:
            phase_counts[event.phase] = phase_counts.get(event.phase, 0) + 1

        return {
            "monitoring_duration_seconds": self.system_metrics[-1].timestamp - self.system_metrics[0].timestamp,
            "metrics_collected": len(self.system_metrics),
            "events_logged": len(self.events),
            "average_cpu_percent": cpu_avg,
            "peak_cpu_percent": cpu_peak,
            "average_memory_mb": memory_avg,
            "peak_memory_mb": memory_peak,
            "average_memory_percent": memory_percent_avg,
            "event_types": event_counts,
            "phases": phase_counts,
        }

    def _monitoring_loop(self, interval_seconds: float):
        """Background monitoring loop."""
        while self.monitoring_active:
            try:
                metrics = self._collect_system_metrics()
                if metrics:
                    self.system_metrics.append(metrics)

                    # Check thresholds
                    if metrics.memory_mb > self.memory_threshold_mb:
                        self._trigger_alert("high_memory", {
                            "current_mb": metrics.memory_mb,
                            "threshold_mb": self.memory_threshold_mb
                        })

                    if metrics.cpu_percent > self.cpu_threshold_percent:
                        self._trigger_alert("high_cpu", {
                            "current_percent": metrics.cpu_percent,
                            "threshold_percent": self.cpu_threshold_percent
                        })

            except Exception as e:
                self.logger.error(f"Monitoring error: {e}")

            time.sleep(interval_seconds)

    def _collect_system_metrics(self) -> Optional[SystemMetrics]:
        """Collect current system metrics."""
        if not HAS_PSUTIL:
            return None

        try:
            process = psutil.Process()
            cpu_percent = process.cpu_percent()
            memory_info = process.memory_info()
            memory_mb = memory_info.rss / 1024 / 1024

            # System-wide memory
            system_memory = psutil.virtual_memory()
            memory_percent = system_memory.percent

            # Disk usage
            disk_usage = psutil.disk_usage('/')
            disk_percent = disk_usage.percent

            # Network connections
            connections = len(psutil.net_connections())

            return SystemMetrics(
                timestamp=time.time(),
                cpu_percent=cpu_percent,
                memory_mb=memory_mb,
                memory_percent=memory_percent,
                disk_usage_percent=disk_percent,
                network_connections=connections
            )

        except Exception as e:
            self.logger.error(f"Failed to collect system metrics: {e}")
            return None

    def _check_alerts(self, event: PipelineEvent):
        """Check event for alert conditions."""
        if event.event_type == "error":
            self._trigger_alert("pipeline_error", {
                "phase": event.phase,
                "message": event.message,
                "metadata": event.metadata
            })

        elif event.event_type == "timeout":
            self._trigger_alert("pipeline_timeout", {
                "phase": event.phase,
                "message": event.message
            })

        elif event.event_type == "memory_limit":
            self._trigger_alert("memory_limit_exceeded", {
                "phase": event.phase,
                "current_mb": event.metadata.get("current_mb", 0),
                "limit_mb": event.metadata.get("limit_mb", 0)
            })

    def _trigger_alert(self, alert_type: str, data: Dict[str, Any]):
        """Trigger alert callbacks."""
        for callback in self.alert_callbacks:
            try:
                callback(alert_type, data)
            except Exception as e:
                self.logger.error(f"Alert callback failed: {e}")

    def _write_event_to_file(self, event: PipelineEvent):
        """Write event to log file."""
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                timestamp = datetime.fromtimestamp(event.timestamp).isoformat()
                log_entry = {
                    "timestamp": timestamp,
                    "event_type": event.event_type,
                    "phase": event.phase,
                    "message": event.message,
                    "metadata": event.metadata
                }
                f.write(f"{timestamp} | {event.event_type} | {event.phase} | {event.message}\n")
        except Exception as e:
            self.logger.error(f"Failed to write event to file: {e}")


class MonitoringContext:
    """Context manager for pipeline monitoring."""

    def __init__(self, monitor: PipelineMonitor, phase: str):
        """Initialize monitoring context."""
        self.monitor = monitor
        self.phase = phase
        self.start_time = None

    def __enter__(self):
        """Enter monitoring context."""
        self.start_time = time.time()
        self.monitor.log_event("phase_start", self.phase, f"Starting {self.phase} phase")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit monitoring context."""
        end_time = time.time()
        duration = end_time - (self.start_time or end_time)

        if exc_type:
            self.monitor.log_event("phase_error", self.phase,
                                 f"{self.phase} phase failed: {exc_val}",
                                 duration_seconds=duration,
                                 error_type=str(exc_type))
        else:
            self.monitor.log_event("phase_complete", self.phase,
                                 f"{self.phase} phase completed successfully",
                                 duration_seconds=duration)


def default_alert_handler(alert_type: str, data: Dict[str, Any]):
    """Default alert handler that logs alerts."""
    logger = logging.getLogger(__name__)
    logger.warning(f"ALERT [{alert_type}]: {data}")


# Global monitor instance
_global_monitor = None


def get_global_monitor() -> PipelineMonitor:
    """Get or create global monitor instance."""
    global _global_monitor
    if _global_monitor is None:
        _global_monitor = PipelineMonitor()
        _global_monitor.add_alert_callback(default_alert_handler)
    return _global_monitor