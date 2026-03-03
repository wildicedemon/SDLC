"""Capability mapping index updater.

Ensures that every decision card has a corresponding
:class:`~corpus.db.models.CapabilityMapping` entry so the retrieval
layer can efficiently look up decisions by capability keyword.

Key function: :func:`update_indices`.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


def update_indices(session: Session, decision_ids: list[str]) -> None:
    """Create missing capability-mapping entries for the given decision cards.

    For each *decision_id*, checks whether a mapping already exists
    for the card's capability.  If not, a new
    :class:`~corpus.db.models.CapabilityMapping` row is inserted
    using the first provenance reference as the domain.

    Args:
        session: Active SQLAlchemy session.
        decision_ids: Decision card IDs to ensure mappings for.
    """
    repo = CorpusRepository(session)

    for did in decision_ids:
        card = repo.get_decision_card(did)
        if card is None:
            continue

        capability = str(card.capability)
        existing = repo.list_capability_mappings(capability=capability)
        existing_decision_ids = {str(m.decision_id) for m in existing}

        if did not in existing_decision_ids:
            # Derive domain from the first provenance ref; fall back to "unknown"
            domain_tags = str(card.provenance_refs).split(",")[0].strip() if card.provenance_refs else "unknown"
            repo.create_capability_mapping(
                capability=capability,
                decision_id=did,
                domain=domain_tags,
            )

    session.flush()
