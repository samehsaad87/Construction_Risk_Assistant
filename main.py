from dotenv import load_dotenv
from openai import OpenAI
from datetime import date
from pathlib import Path

# Create the output folder
output_folder = Path("risk_reports")
output_folder.mkdir(exist_ok=True)

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(timeout=30.0, max_retries=0)

print("Construction Risk Assistant started successfully!")

while True:
    risk_description = input("Describe the construction risk: ")

    risk_id = input("Enter the risk ID: ")

    risk_date = date.today()

    report_file = output_folder / f"{risk_id}.txt"

    try:
        response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
You are a construction project risk management assistant.

Risk ID: {risk_id}
    
Analyze the following construction project risk:

{risk_description}

Provide the analysis in the following format:

## Risk Description
## Probability
## Impact
## Risk Level

## Preventive Actions
Use bullet points.

## Response Plan
Use bullet points.

## Project Manager Recommendation
Provide one practical recommendation.
"""

    )

        print(f"\nRisk Analysis - {risk_id}:\n")
        print(f"Date Recorded: {risk_date}\n")
        print(response.output_text)

        with open(report_file, "w", encoding="utf-8") as file:
            file.write(f"Risk Analysis - {risk_id}\n")
            file.write(f"Date Recorded: {risk_date}\n\n")
            file.write(response.output_text)
        print(f"\nReport saved to: {report_file}")

    except Exception as error:
        print("\nAn error occurred:")
        print(error)

    another_risk = input("\nDo you want to analyze another risk? (yes/no): ")

    if another_risk.lower() != "yes":
        print("\nConstruction Risk Assistant finished.")
        break