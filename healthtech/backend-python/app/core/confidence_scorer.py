SEVERITY_WEIGHT = {"high": 1.0, "moderate": 0.75, "low": 0.4}
GUIDELINE_SUPPORT_BY_GENE = {
    "CYP2D6": 1.0,
    "CYP2C19": 1.0,
    "CYP2C9": 0.95,
    "SLCO1B1": 0.9,
    "TPMT": 0.95,
    "DPYD": 0.95,
    "N/A": 0.5,
}


def compute_confidence(recommendations: list[dict[str, str]], variants_count: int, drugs_count: int) -> dict:
    if not recommendations:
        return {
            "score": 0.0,
            "breakdown": {
                "variant_impact": 0.0,
                "gene_drug_relevance": 0.0,
                "guideline_support": 0.0,
                "data_completeness": 0.0,
            },
        }

    variant_impact = sum(SEVERITY_WEIGHT.get(item["severity"], 0.4) for item in recommendations) / len(recommendations)
    actionable_drugs = {
        item["drug"] for item in recommendations if item["risk_label"] != "No Actionable PGx Rule Found"
    }
    gene_drug_relevance = min(1.0, len(actionable_drugs) / max(drugs_count, 1))
    guideline_support = sum(GUIDELINE_SUPPORT_BY_GENE.get(item["gene"], 0.5) for item in recommendations) / len(recommendations)
    data_completeness = min(1.0, variants_count / 3)

    score = (
        (variant_impact * 0.30)
        + (gene_drug_relevance * 0.30)
        + (guideline_support * 0.25)
        + (data_completeness * 0.15)
    ) * 100

    return {
        "score": round(score, 1),
        "breakdown": {
            "variant_impact": round(variant_impact, 2),
            "gene_drug_relevance": round(gene_drug_relevance, 2),
            "guideline_support": round(guideline_support, 2),
            "data_completeness": round(data_completeness, 2),
        },
    }
