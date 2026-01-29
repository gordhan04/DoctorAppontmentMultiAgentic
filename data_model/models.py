import re
from pydantic import BaseModel,Field,field_validator

class DateTimeModel(BaseModel):
    date:str = Field(description="properly formatted date",pattern=r"^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$")

    @field_validator("date")
    def check_format_date(cls,v):
        if not re.match(r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$', v): # Ensure DD-MM-YYYY HH:MM Format
            raise ValueError("The date should be in format 'DD-MM-YYYY HH:MM'")
        return v
class DateModel(BaseModel):
    date:str = Field(description="Properly formatted date",pattern=r'^\d{2}-\d{2}-\d{4}$')

    @field_validator("date")
    def check_format_date(cls,v):
        if not re.match(r'^\d{2}-\d{2}-\d{4}$', v):
            raise ValueError("The date should be in format 'DD-MM-YYYY'") # Ensure DD-MM-YYYY Format
        return v
class IdentificationNumberModel(BaseModel):
    id : int = Field(description="Identification number (7 to 8 digit long)")
    
    @field_validator("id")
    def check_id_format(cls,v):
        if not re.match(r'^\d{7,8}$', str(v)):  # Convert to string before matching
            raise ValueError("The ID number should be a 7 or 8-digit number")
        return v