from pydantic import BaseModel, Field, field_validator


class AnalyzeRequest(BaseModel):
    vcf_text: str = Field(..., min_length=1)
    drugs: list[str] = Field(..., min_length=1)

    @field_validator("drugs")
    @classmethod
    def normalize_drugs(cls, value: list[str]) -> list[str]:
        normalized = [drug.strip().upper() for drug in value if drug and drug.strip()]
        if not normalized:
            raise ValueError("At least one drug is required")
        return normalized
