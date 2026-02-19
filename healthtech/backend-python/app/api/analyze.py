from fastapi import APIRouter

from app.core.confidence_scorer import compute_confidence
from app.core.llm_explainer import build_explanation
from app.core.phenotype_mapper import infer_phenotype
from app.core.rule_engine import evaluate_drug_rules
from app.core.vcf_parser import parse_vcf_text
from app.schemas.input_schema import AnalyzeRequest
from app.schemas.output_schema import AnalyzeResponse

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    parsed_variants = parse_vcf_text(request.vcf_text)

    matched_variants = []
    gene_phenotypes = []
    seen = set()

    for variant in parsed_variants:
        phenotype = infer_phenotype(variant["gene"], variant["star"])
        entry = {
            "gene": variant["gene"],
            "star_allele": variant["star"],
            "rsid": variant["rs"],
            "phenotype": phenotype,
        }
        matched_variants.append(entry)

        gene_key = (variant["gene"], phenotype)
        if gene_key not in seen:
            seen.add(gene_key)
            gene_phenotypes.append({"gene": variant["gene"], "phenotype": phenotype})

    recommendations = evaluate_drug_rules(request.drugs, gene_phenotypes)
    confidence = compute_confidence(recommendations, len(matched_variants), len(request.drugs))
    explanation = build_explanation(request.drugs, matched_variants, recommendations, confidence)

    return AnalyzeResponse(
        patient_summary={
            "genes_detected": sorted(list({variant['gene'] for variant in parsed_variants})),
            "variants_considered": len(matched_variants),
            "drugs_requested": request.drugs,
        },
        matched_variants=matched_variants,
        drug_recommendations=recommendations,
        confidence=confidence,
        explanation=explanation,
        disclaimer=(
            "Prototype clinical decision-support output only. "
            "Not for standalone diagnosis or treatment selection."
        ),
    )
