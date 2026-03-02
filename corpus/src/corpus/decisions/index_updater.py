from __future__ import annotations

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


def update_indices(session: Session, decision_ids: list[str]) -> None:
    repo = CorpusRepository(session)

    for did in decision_ids:
        card = repo.get_decision_card(did)
        if card is None:
            continue

        capability = str(card.capability)
        existing = repo.list_capability_mappings(capability=capability)
        existing_decision_ids = {str(m.decision_id) for m in existing}

        if did not in existing_decision_ids:
            domain_tags = str(card.provenance_refs).split(",")[0].strip() if card.provenance_refs else "unknown"
            repo.create_capability_mapping(
                capability=capability,
                decision_id=did,
                domain=domain_tags,
            )

    session.flush()
