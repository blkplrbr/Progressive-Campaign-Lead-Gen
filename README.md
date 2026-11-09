# Progressive-Campaign-Lead-Gen
## Project Overview
Developed a lightweight, zero-dependency Python pipeline for a political consulting firm to aggregate, clean, and score B2B leads. The script takes raw, disparate data from multiple sources (IRS 990 filings, OpenFEC, Meta Ad Library) and outputs a deduplicated, prioritized outreach database.

## The Problem
The consulting firm needed to pitch its tech services to progressive organizations. However, the raw data was messy: the same organization would appear multiple times across different datasets with varying URLs, and the firm needed a way to know which organizations were high-value targets versus low-budget grassroots groups.

## Technical Stack
*   **Language:** Python (Zero dependencies, standard library only)
*   **Libraries:** `csv`, `re`
*   **Output:** Automated `.csv` file with an engineered "Pitch Strategy" column.

## Methodology & Code Architecture

### 1. Regex Data Cleansing
Built a custom function (`clean_domain`) to standardize unstructured URLs. It strips out `https://`, `www.`, and trailing path directories to isolate the root domain, ensuring accurate entity matching.

### 2. Dictionary-Based Deduplication & Aggregation
Because organizations appeared multiple times across different data sources, I built a deduplication engine using a Python dictionary keyed by the cleaned domain. If a domain appeared twice, the script merged the data:
*   Appended the new source to a list of known sources.
*   Summed the `Total_Spend` across all filings.

### 3. Dynamic Pitch Routing (The Lead Score)
To save the sales team time, I engineered custom logic to assign a specific sales pitch based on the organization's profile:
*   **White-Glove Tier:** If the org spent > $500,000 OR appeared in 3+ data sources, they were flagged for a high-touch pitch (VAN Data Sync & Field Turf Optimization).
*   **Growth Tier:** All others were flagged for a standard pitch (Direct P2P Text-Banking & Donor Mobilization).

### 4. Data Export
Utilized the `csv` module to output the cleaned, aggregated, and scored data into `progressive_campaign_leads.csv`, ready for immediate use by the business development team.

## Business Impact
*   Transformed messy, multi-source political data into a clean, actionable sales pipeline.
*   Automated the lead qualification process, ensuring sales reps prioritized organizations with the highest spending power.
*   Created a repeatable, zero-dependency script that the firm can run anytime they need to refresh their lead list.
