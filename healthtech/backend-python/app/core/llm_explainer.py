def build_explanation(drugs: list[str], matched_variants: list[dict], recommendations: list[dict], confidence: dict) -> str:
    variant_chunks = [
        f"{item['gene']} {item['star_allele']} ({item['phenotype']})"
        for item in matched_variants
    ]
    variant_text = ", ".join(variant_chunks) if variant_chunks else "no actionable variants"

    recommendation_chunks = [
        f"{item['drug']}: {item['risk_label']} ({item['recommendation']})"
        for item in recommendations
    ]
    recommendation_text = "; ".join(recommendation_chunks)

    return (
        "This pharmacogenomic decision-support summary is based on deterministic parsing of the provided "
        f"VCF and fixed gene-drug rules for requested drugs ({', '.join(drugs)}). "
        f"Detected profile: {variant_text}. "
        f"Rule outcome: {recommendation_text}. "
        f"Overall confidence score is {confidence['score']}/100, reflecting evidence weighting for variant impact, "
        "gene-drug relevance, guideline support, and data completeness. "
        "Interpretation should be reviewed by a licensed clinician before any treatment decision."
    )
