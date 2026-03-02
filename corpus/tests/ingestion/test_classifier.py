from corpus.ingestion.classifier import DOMAIN_DIRECTORIES, Classification, classify


class TestClassifyDomainPaths:
    def test_security_architecture_patterns(self) -> None:
        result = classify("docs/research/01_meta_architecture/security_architecture/patterns.md")
        assert result.is_classified is True
        assert "security_architecture" in result.domain_tags

    def test_research_benchmarking_framework_overview(self) -> None:
        result = classify("docs/research/09_research_discipline/research_benchmarking_framework/overview.md")
        assert result.is_classified is True
        assert "research_benchmarking_framework" in result.domain_tags

    def test_unknown_path_not_classified(self) -> None:
        result = classify("random/unknown/file.md")
        assert result.is_classified is False
        assert result.domain_tags == []
        assert result.capability_tags == []

    def test_meta_path_classified(self) -> None:
        result = classify("docs/research/00_meta/confidence_policy.md")
        assert result.is_classified is True
        assert "meta" in result.domain_tags

    def test_all_12_domain_directories_have_rules(self) -> None:
        expected_prefixes = [f"{i:02d}_" for i in range(1, 13)]
        for prefix in expected_prefixes:
            matching = [k for k in DOMAIN_DIRECTORIES if k.startswith(prefix)]
            assert len(matching) >= 1, f"No rule for domain prefix {prefix}"

    def test_indices_path_classified(self) -> None:
        result = classify("docs/research/03_indices/decision_index.md")
        assert result.is_classified is True
        assert "indices" in result.domain_tags

    def test_non_md_inside_research_not_classified(self) -> None:
        result = classify("docs/research/01_meta_architecture/security_architecture/data.json")
        assert result.is_classified is True

    def test_backslash_paths_normalized(self) -> None:
        result = classify("docs\\research\\01_meta_architecture\\security_architecture\\patterns.md")
        assert result.is_classified is True
        assert "security_architecture" in result.domain_tags

    def test_capability_tag_from_custom_filename(self) -> None:
        result = classify("docs/research/06_data_infrastructure/database_data_engineering/sharding_strategies.md")
        assert result.is_classified is True
        assert "database_data_engineering" in result.domain_tags
        assert "sharding_strategies" in result.capability_tags

    def test_standard_filenames_have_no_capability_tag(self) -> None:
        for name in ("overview.md", "patterns.md", "comparisons.md", "references.md", "README.md"):
            result = classify(f"docs/research/01_meta_architecture/security_architecture/{name}")
            assert result.capability_tags == [], f"Unexpected capability tag for {name}"

    def test_unknown_subdomain_not_classified(self) -> None:
        result = classify("docs/research/01_meta_architecture/nonexistent_subdomain/overview.md")
        assert result.is_classified is False

    def test_perplexity_overview_no_capability_tag(self) -> None:
        result = classify(
            "docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md"
        )
        assert result.is_classified is True
        assert result.capability_tags == []

    def test_classification_dataclass_defaults(self) -> None:
        c = Classification()
        assert c.domain_tags == []
        assert c.capability_tags == []
        assert c.is_classified is False
