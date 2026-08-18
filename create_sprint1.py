import os
import json
import time

JOBS_DB_PATH = "/Users/jordanleprunenec/.gemini/antigravity/scratch/espace5_checklist/jobs_database.json"

# Les 20 postes sélectionnés (hors Atos)
TOP_20_JOBS = [
    {
        "id": "sprint1_01",
        "company": "Amazon Web Services (AWS)",
        "title": "GenAI Sales Specialist, AWS Specialists Team",
        "location": "Courbevoie (92) / Paris",
        "job_url": "https://fr.linkedin.com/jobs/view/genai-sales-specialist-aws-specialists-team-at-amazon-web-services-aws-4446832565",
        "type": "CDI",
        "match_score": "98%",
        "pitch": "Expert GTM & prospection IA formé chez Alegria.tech, j'accompagne l'adoption des solutions d'IA générative et de cloud computing auprès des grands comptes en m'appuyant sur des cycles de vente structurés et une forte maîtrise technique."
    },
    {
        "id": "sprint1_02",
        "company": "Amazon Web Services (AWS)",
        "title": "GenAI Sales Specialist, AWS Specialist Team France",
        "location": "Courbevoie (92) / Paris",
        "job_url": "https://fr.linkedin.com/jobs/view/genai-sales-specialist-aws-specialist-team-france-at-amazon-web-services-aws-4446162470",
        "type": "CDI",
        "match_score": "97%",
        "pitch": "Spécialiste de l'acquisition B2B et des workflows automatisés (n8n), je pilote la qualification et le closing d'infrastructures IA Cloud auprès de décideurs C-Level."
    },
    {
        "id": "sprint1_03",
        "company": "Craft AI",
        "title": "Account Executive IA",
        "location": "Paris (75)",
        "job_url": "https://fr.linkedin.com/jobs/view/account-executive-ia-at-craft-ai-4448755686",
        "type": "CDI",
        "match_score": "96%",
        "pitch": "Expérience confirmée chez GM Capital dans la vente de solutions complexes et l'orchestration de pipelines commerciaux pour des plateformes d'IA d'entreprise."
    },
    {
        "id": "sprint1_04",
        "company": "Neural Concept",
        "title": "Account Executive - France (Deep Learning & Engineering AI)",
        "location": "Paris (75)",
        "job_url": "https://fr.linkedin.com/jobs/view/account-executive-france-at-neural-concept-4385457517",
        "type": "CDI",
        "match_score": "95%",
        "pitch": "Spécialisé dans la prospection multicanale et l'évangélisation technologique d'outils d'IA de rupture auprès de directeurs techniques et R&D."
    },
    {
        "id": "sprint1_05",
        "company": "XXII",
        "title": "Senior Enterprise Account Executive – Robotics & Physical AI",
        "location": "Puteaux (92)",
        "job_url": "https://fr.linkedin.com/jobs/view/senior-enterprise-account-executive-%E2%80%93-robotics-physical-ai-at-xxii-4435038970",
        "type": "CDI",
        "match_score": "95%",
        "pitch": "Chasseur B2B aguerri, capable d'adresser des cycles de vente longs et stratégiques sur des solutions d'IA visuelle et de vision par ordinateur."
    },
    {
        "id": "sprint1_06",
        "company": "SoftwareOne",
        "title": "Microsoft Solution Sales Specialist - Data & AI",
        "location": "Paris (75)",
        "job_url": "https://fr.linkedin.com/jobs/view/microsoft-solution-sales-specialist-data-ai-at-softwareone-4449764789",
        "type": "CDI",
        "match_score": "94%",
        "pitch": "Maîtrise de l'écosystème cloud/data et déploiement de stratégies d'acquisition ciblées sur les directeurs métiers et DSI."
    },
    {
        "id": "sprint1_07",
        "company": "Inetum",
        "title": "Sales Specialist AI Business Solutions Microsoft H/F",
        "location": "Saint-Ouen (93)",
        "job_url": "https://fr.linkedin.com/jobs/view/sales-specialist-ai-business-solutions-microsoft-h-f-at-inetum-4400591201",
        "type": "CDI",
        "match_score": "94%",
        "pitch": "Compétences clés en développement d'affaires et valorisation ROI des cas d'usage IA et automatisation pour grands comptes."
    },
    {
        "id": "sprint1_08",
        "company": "NTT DATA, Inc.",
        "title": "Data & AI Technology Sales Specialist",
        "location": "Paris (75)",
        "job_url": "https://fr.linkedin.com/jobs/view/data-ai-technology-sales-specialist-at-ntt-data-inc-4426777859",
        "type": "CDI",
        "match_score": "93%",
        "pitch": "Structuration de partenariats technologiques et pilotage commercial de bout en bout sur des projets Data & IA d'envergure."
    },
    {
        "id": "sprint1_09",
        "company": "DXC Technology",
        "title": "Consultative AI Sales Professional",
        "location": "Paris (75)",
        "job_url": "https://fr.linkedin.com/jobs/view/consultative-ai-sales-professional-at-dxc-technology-4371314015",
        "type": "CDI",
        "match_score": "93%",
        "pitch": "Approche consultative data-driven, de la cartographie des besoins à la contractualisation de solutions d'IA d'entreprise."
    },
    {
        "id": "sprint1_10",
        "company": "Qdrant",
        "title": "Business Development Representative (EMEA) - Vector Search & AI",
        "location": "Paris / Remote",
        "job_url": "https://qdrant.tech/careers/",
        "type": "CDI / Remote",
        "match_score": "92%",
        "pitch": "Spécialiste de l'outreach technique et de l'acquisition de développeurs et entreprises intégrant des modèles de recherche vectorielle et RAG."
    },
    {
        "id": "sprint1_11",
        "company": "SCC France",
        "title": "Account Manager Specialist AI Solutions (H/F)",
        "location": "Nanterre (92)",
        "job_url": "https://fr.linkedin.com/jobs/view/account-manager-specialist-ai-solutions-h-f-at-scc-france-4447385966",
        "type": "CDI",
        "match_score": "92%",
        "pitch": "Fidélisation et conquête de nouveaux comptes sur des offres d'infrastructures et d'usages IA à forte valeur ajoutée."
    },
    {
        "id": "sprint1_12",
        "company": "ATECNA",
        "title": "Business Developer – Projets & Innovation IA (F/H)",
        "location": "Paris (75)",
        "job_url": "https://fr.linkedin.com/jobs/view/business-developer-%E2%80%93-projets-innovation-ia-f-h-at-atecna-4448281144",
        "type": "CDI",
        "match_score": "91%",
        "pitch": "Développement commercial agile axé sur les projets d'innovation et d'intégration de briques IA pour entreprises en transformation."
    },
    {
        "id": "sprint1_13",
        "company": "Witivio - AI Solutions for Microsoft 365",
        "title": "BDR Produit – SaaS, IA & Solutions Microsoft",
        "location": "Paris / Remote",
        "job_url": "https://fr.linkedin.com/jobs/view/business-development-representative-produit-%E2%80%93-saas-ia-solutions-microsoft-at-witivio-ai-solutions-for-microsoft-365-4449768652",
        "type": "CDI",
        "match_score": "91%",
        "pitch": "Génération d'opportunités qualifiées et prospection automatisée multicanale pour éditeur SaaS IA."
    },
    {
        "id": "sprint1_14",
        "company": "ElevenLabs",
        "title": "Deployment Strategist - France / Expansion",
        "location": "Paris / Remote",
        "job_url": "https://fr.linkedin.com/jobs/view/deployment-strategist-france-global-expansion-at-elevenlabs-4449760012",
        "type": "CDI / Remote",
        "match_score": "90%",
        "pitch": "Accélération du Go-To-Market et intégration de technologies de synthèse vocale IA auprès d'éditeurs et de médias."
    },
    {
        "id": "sprint1_15",
        "company": "WOLD",
        "title": "Business Developer - Data, IA, Digital",
        "location": "Paris (75)",
        "job_url": "https://fr.linkedin.com/jobs/view/business-developer-data-ia-digital-paris-cdi-at-wold-4446654891",
        "type": "CDI",
        "match_score": "90%",
        "pitch": "Prospection et qualification de projets de conseil et d'ingénierie Data & IA."
    },
    {
        "id": "sprint1_16",
        "company": "Daiteo",
        "title": "Sales Full Cycle : Prospection & Closing",
        "location": "Paris (75)",
        "job_url": "https://fr.linkedin.com/jobs/view/un-e-sales-full-cycle-prospection-cycle-de-vente-suivi-at-daiteo-4448753210",
        "type": "CDI",
        "match_score": "89%",
        "pitch": "Gestion intégrale du cycle commercial, de la génération de leads au closing contractuel."
    },
    {
        "id": "sprint1_17",
        "company": "Capgemini Engineering",
        "title": "Sales Developer AI & Digital",
        "location": "Issy-les-Moulineaux (92)",
        "job_url": "https://fr.linkedin.com/jobs/view/sales-developer-at-capgemini-engineering-4448283311",
        "type": "CDI",
        "match_score": "89%",
        "pitch": "Développement d'opportunités commerciales sur des projets industriels et numériques de pointe."
    },
    {
        "id": "sprint1_18",
        "company": "Botify",
        "title": "Account Executive, SEMEA",
        "location": "Paris (75)",
        "job_url": "https://fr.linkedin.com/jobs/view/account-executive-semea-at-botify-4446653011",
        "type": "CDI",
        "match_score": "88%",
        "pitch": "Closing de comptes enterprise pour plateforme SaaS d'optimisation par IA des moteurs de recherche."
    },
    {
        "id": "sprint1_19",
        "company": "ILLUIN Technology",
        "title": "BDR (F/H) - Spécialiste IA & NLP",
        "location": "Paris (75)",
        "job_url": "https://fr.linkedin.com/jobs/view/bdr-f-h-at-illuin-technology-4447384102",
        "type": "CDI",
        "match_score": "88%",
        "pitch": "Prospection ciblée sur les directions innovation et métiers pour projets d'IA conversationnelle et générative."
    },
    {
        "id": "sprint1_20",
        "company": "Databricks",
        "title": "Lakebase Sales Associate Director",
        "location": "Paris (75)",
        "job_url": "https://fr.linkedin.com/jobs/view/lakebase-sales-associate-director-at-databricks-4448285520",
        "type": "CDI",
        "match_score": "87%",
        "pitch": "Vente de solutions de données et d'IA unifiées auprès des grands comptes français et internationaux."
    }
]

# Sauvegarde du fichier Sprint 1
with open("/Users/jordanleprunenec/.gemini/antigravity/scratch/espace5_checklist/sprint1_top20.json", "w", encoding="utf-8") as f:
    json.dump(TOP_20_JOBS, f, ensure_ascii=False, indent=2)

print("✅ Fichier sprint1_top20.json créé avec succès !")
