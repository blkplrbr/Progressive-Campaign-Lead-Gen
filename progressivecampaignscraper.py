import csv
import re

def clean_domain(domain):
    if not domain:
        return ""
    d = str(domain).lower().strip()
    d = re.sub(r"^https?://", "", d)
    d = re.sub(r"^www\.", "", d)
    return d.split("/")[0]

def main():
    print("🏄‍♂️ Running Zero-Dependency Campaign Pipeline...")

    # Data nets
    raw_data = [
        {"org_name": "Sunrise Movement Education Fund", "source": "IRS 990", "domain": "sunrisemovement.org", "spend": 850000, "state": "DC", "cause": "Climate & GND"},
        {"org_name": "Sunrise Movement PAC", "source": "OpenFEC", "domain": "sunrisemovement.org", "spend": 125000, "state": "DC", "cause": "Climate & GND"},
        {"org_name": "Sunrise Movement", "source": "Meta Ad Library", "domain": "sunrisemovement.org", "spend": 45000, "state": "DC", "cause": "Climate & GND"},
        {"org_name": "Indivisible Project Inc", "source": "IRS 990", "domain": "indivisible.org", "spend": 1200000, "state": "DC", "cause": "Grassroots Democracy"},
        {"org_name": "Working Families Organization Inc", "source": "IRS 990", "domain": "workingfamilies.org", "spend": 600000, "state": "NY", "cause": "Labor & Economic Justice"},
        {"org_name": "Working Families Party National Committee", "source": "OpenFEC", "domain": "workingfamilies.org", "spend": 450000, "state": "NY", "cause": "Labor & Economic Justice"},
        {"org_name": "NC Reproductive Freedom Coalition", "source": "Meta Ad Library", "domain": "ncreprofreedom.org", "spend": 32000, "state": "NC", "cause": "Reproductive Rights"},
        {"org_name": "NC Reproductive Freedom Coalition Ballot Committee", "source": "State Ethics", "domain": "ncreprofreedom.org", "spend": 150000, "state": "NC", "cause": "Reproductive Rights"}
    ]

    # Domain Deduplication Dictionary
    deduped = {}
    for row in raw_data:
        dom = clean_domain(row['domain'])
        if dom not in deduped:
            deduped[dom] = {
                'Primary_Org_Name': row['org_name'],
                'Domain': dom,
                'Sources': {row['source']},
                'Total_Spend': int(row['spend']),
                'State': row['state'],
                'Cause': row['cause']
            }
        else:
            deduped[dom]['Sources'].add(row['source'])
            deduped[dom]['Total_Spend'] += int(row['spend'])

    # Export to CSV (Opens directly in Excel)
    output_filename = "progressive_campaign_leads.csv"
    
    fieldnames = ['Primary_Org_Name', 'Domain', 'Sources', 'Total_Spend', 'State', 'Cause', 'Pitch_Strategy']
    
    with open(output_filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for dom, info in deduped.items():
            sources_str = ", ".join(sorted(info['Sources']))
            spend = info['Total_Spend']
            cause = info['Cause']
            
            # Simple Tier Logic
            if spend >= 500000 or len(info['Sources']) >= 3:
                pitch = f"White-Glove Tier: VAN Data Sync & Field Turf Optimization for {cause}"
            else:
                pitch = f"Growth Tier: Direct P2P Text-Banking & Donor Mobilization for {cause}"

            writer.writerow({
                'Primary_Org_Name': info['Primary_Org_Name'],
                'Domain': info['Domain'],
                'Sources': sources_str,
                'Total_Spend': f"${spend:,}",
                'State': info['State'],
                'Cause': cause,
                'Pitch_Strategy': pitch
            })

    print(f"🚀 SUCCESS! Generated '{output_filename}' using built-in Python.")

if __name__ == "__main__":
    main()