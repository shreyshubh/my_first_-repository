from pydantic import BaseModel, ConfigDict, Field, field_validator


class AnalyzeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    vcf_text: str = Field(..., min_length=1)
    drugs: list[str] = Field(..., min_length=1)

    @field_validator("drugs")
    @classmethod
    def normalize_drugs(cls, value: list[str]) -> list[str]:
        normalized = [drug.strip().upper() for drug in value if drug and drug.strip()]
        deduplicated: list[str] = []
        seen = set()
        for drug in normalized:
            if drug not in seen:
                seen.add(drug)
                deduplicated.append(drug)

        if not deduplicated:
            raise ValueError("At least one drug is required")

        return deduplicated
