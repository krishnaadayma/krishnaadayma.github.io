class InternationalTradeCompliance:
    def __init__(self):
        self.trade_data = {
            "countries": {
                "Italy": {
                    "general": {
                        "country_name": "Italian Republic",
                        "capital": "Rome",
                        "currency": "Euro (EUR)",
                        "iso_currency_code": "EUR",
                        "official_language": "Italian",
                        "country_code_iso_3166": "IT",
                        "eu_member": True,
                        "gcc_member": False
                    },
                    "trade_logistics": {
                        "primary_ports": ["Genoa", "Trieste", "Gioia Tauro", "Naples", "La Spezia"],
                        "primary_airports": ["Rome Fiumicino (FCO)", "Milan Malpensa (MXP)"],
                        "hs_system": "EU Combined Nomenclature (CN) - based on HS",
                        "incoterms": "Commonly used: FCA, EXW, CIF, DAP",
                        "document_standard": "EU Standardized (e.g., EORI number required)",
                        "ease_of_doing_rank": 58,
                        "lpi_score": 3.8
                    },
                    "documentation_requirements": {
                        "commercial_invoice": True,
                        "packing_list": True,
                        "certificate_of_origin": "Often required, EUR.1 for preferential treatment",
                        "bill_of_lading_awb": True,
                        "customs_declaration": "EU Single Administrative Document (SAD)",
                        "import_license": "Required for specific goods (e.g., firearms, pharmaceuticals)",
                        "phyto_sanitary_certificate": "Required for plants, plant products, certain foods",
                        "insurance_documents": "Typically arranged by seller for CIF terms",
                        "required_identifiers": "EORI Number (Economic Operators Registration and Identification)"
                    },
                    "regulatory_environment": {
                        "customs_procedure": "Aligned with EU Customs Union (TARIC database)",
                        "import_tariffs": "EU Common External Tariff (CET)",
                        "vat_on_imports": 22.0,
                        "restricted_items": ["Dangerous goods", "Counterfeit goods", "Protected species (CITES)"],
                        "standards": "CE Marking required for many products"
                    }
                },
                "India": {
                    "general": {
                        "country_name": "Republic of India",
                        "capital": "New Delhi",
                        "currency": "Indian Rupee (INR)",
                        "iso_currency_code": "INR",
                        "official_language": "Hindi, English",
                        "country_code_iso_3166": "IN",
                        "eu_member": False,
                        "gcc_member": False
                    },
                    "trade_logistics": {
                        "primary_ports": ["Jawaharlal Nehru (Nhava Sheva)", "Mundra", "Chennai", "Visakhapatnam", "Kolkata"],
                        "primary_airports": ["Delhi (DEL)", "Mumbai (BOM)", "Chennai (MAA)", "Bangalore (BLR)"],
                        "hs_system": "Indian Trade Classification (Harmonized System) - ITC(HS)",
                        "incoterms": "Commonly used: FOB, EXW, CIF",
                        "document_standard": "Indian Customs Electronic Declaration",
                        "ease_of_doing_rank": 63,
                        "lpi_score": 3.2
                    },
                    "documentation_requirements": {
                        "commercial_invoice": True,
                        "packing_list": True,
                        "certificate_of_origin": "Often required, specific formats for preferential treaties",
                        "bill_of_lading_awb": True,
                        "customs_declaration": "Electronic (ICEGATE) - Bill of Entry",
                        "import_license": "Required for restricted items (IRR), many goods under OGL (Open General License)",
                        "phyto_sanitary_certificate": "Required for plants, seeds, livestock products",
                        "insurance_documents": "Typically arranged by importer, except for CIF terms",
                        "required_identifiers": "Import Export Code (IEC) - Mandatory for all importers/exporters"
                    },
                    "regulatory_environment": {
                        "customs_procedure": "Governed by the Customs Act, 1962",
                        "import_tariffs": "Basic Customs Duty (BCD) + Integrated GST (IGST) + Social Welfare Surcharge",
                        "vat_on_imports": "IGST applied (rates vary: 5%, 12%, 18%, 28%)",
                        "restricted_items": ["Animal products", "Firearms", "Gold & Silver bullion", "Certain chemicals"],
                        "standards": "BIS Certification required for many products; FSSAI for food"
                    }
                }
            },
            "bilateral_context": {
                "trade_agreement": "No dedicated bilateral FTA. Trade under WTO MFN rules.",
                "preferential_documents": "Certificate of Origin usually required to claim WTO MFN tariffs.",
                "key_trade_goods": {
                    "india_to_italy": ["Textiles & Apparel", "Leather Goods", "Automotive Parts", "Iron & Steel", "Chemicals", "Rice", "Coffee"],
                    "italy_to_india": ["Machinery & Engines", "Electrical Equipment", "Chemicals & Pharmaceuticals", "Plastics", "Luxury Goods (Fashion, Furniture)", "Wine & Food Products"]
                }
            }
        }

    def display_country_info(self, country_name):
        """Display comprehensive information about a country's trade regulations"""
        if country_name not in self.trade_data["countries"]:
            print(f"Data for {country_name} not found.")
            return
        
        country = self.trade_data["countries"][country_name]
        
        print(f"\n{'='*60}")
        print(f"TRADE COMPLIANCE DATA: {country_name.upper()}")
        print(f"{'='*60}")
        
        # General Information
        print("\n📋 GENERAL INFORMATION:")
        print(f"  • Official Name: {country['general']['country_name']}")
        print(f"  • Capital: {country['general']['capital']}")
        print(f"  • Currency: {country['general']['currency']}")
        print(f"  • ISO Code: {country['general']['country_code_iso_3166']}")
        print(f"  • EU Member: {'Yes' if country['general']['eu_member'] else 'No'}")
        
        # Trade Logistics
        print("\n🚢 TRADE LOGISTICS:")
        print(f"  • Primary Ports: {', '.join(country['trade_logistics']['primary_ports'])}")
        print(f"  • Primary Airports: {', '.join(country['trade_logistics']['primary_airports'])}")
        print(f"  • HS System: {country['trade_logistics']['hs_system']}")
        print(f"  • Common Incoterms: {country['trade_logistics']['incoterms']}")
        print(f"  • Ease of Doing Business Rank: {country['trade_logistics']['ease_of_doing_rank']}")
        print(f"  • LPI Score: {country['trade_logistics']['lpi_score']}")
        
        # Documentation Requirements
        print("\n📄 DOCUMENTATION REQUIREMENTS:")
        docs = country['documentation_requirements']
        for doc, requirement in docs.items():
            if isinstance(requirement, bool):
                status = "Required" if requirement else "Not Required"
                print(f"  • {doc.replace('_', ' ').title()}: {status}")
            else:
                print(f"  • {doc.replace('_', ' ').title()}: {requirement}")
        
        # Regulatory Environment
        print("\n⚖️ REGULATORY ENVIRONMENT:")
        regs = country['regulatory_environment']
        print(f"  • Customs Procedure: {regs['customs_procedure']}")
        print(f"  • Import Tariffs: {regs['import_tariffs']}")
        print(f"  • VAT on Imports: {regs['vat_on_imports']}")
        print(f"  • Restricted Items: {', '.join(regs['restricted_items'])}")
        print(f"  • Standards: {regs['standards']}")

    def display_bilateral_info(self):
        """Display bilateral trade information between Italy and India"""
        bilateral = self.trade_data["bilateral_context"]
        
        print(f"\n{'='*60}")
        print("ITALY-INDIA BILATERAL TRADE INFORMATION")
        print(f"{'='*60}")
        
        print(f"\n📊 TRADE AGREEMENT:")
        print(f"  • {bilateral['trade_agreement']}")
        print(f"  • Preferential Documents: {bilateral['preferential_documents']}")
        
        print(f"\n📦 KEY TRADE GOODS - INDIA TO ITALY:")
        for i, good in enumerate(bilateral['key_trade_goods']['india_to_italy'], 1):
            print(f"  {i}. {good}")
        
        print(f"\n📦 KEY TRADE GOODS - ITALY TO INDIA:")
        for i, good in enumerate(bilateral['key_trade_goods']['italy_to_india'], 1):
            print(f"  {i}. {good}")

    def compare_countries(self, country1, country2):
        """Compare trade regulations between two countries"""
        if country1 not in self.trade_data["countries"] or country2 not in self.trade_data["countries"]:
            print("One or both countries not found in database.")
            return
        
        c1 = self.trade_data["countries"][country1]
        c2 = self.trade_data["countries"][country2]
        
        print(f"\n{'='*60}")
        print(f"COMPARISON: {country1.upper()} vs {country2.upper()}")
        print(f"{'='*60}")
        
        # Compare general information
        print("\n🌍 GENERAL COMPARISON:")
        print(f"  {'Metric':<25} {country1:<20} {country2:<20}")
        print(f"  {'-'*25} {'-'*20} {'-'*20}")
        print(f"  {'Currency':<25} {c1['general']['currency']:<20} {c2['general']['currency']:<20}")
        print(f"  {'EU Member':<25} {'Yes' if c1['general']['eu_member'] else 'No':<20} {'Yes' if c2['general']['eu_member'] else 'No':<20}")
        
        # Compare logistics
        print(f"\n🚢 LOGISTICS COMPARISON:")
        print(f"  • Ease of Business Rank: {c1['trade_logistics']['ease_of_doing_rank']} ({country1}) vs {c2['trade_logistics']['ease_of_doing_rank']} ({country2})")
        print(f"  • LPI Score: {c1['trade_logistics']['lpi_score']} ({country1}) vs {c2['trade_logistics']['lpi_score']} ({country2})")
        
        # Compare VAT/Import Taxes
        print(f"\n💰 TAX COMPARISON:")
        vat1 = c1['regulatory_environment']['vat_on_imports']
        vat2 = c2['regulatory_environment']['vat_on_imports']
        print(f"  • Import VAT/Taxes: {vat1} ({country1}) vs {vat2} ({country2})")

    def run_demo(self):
        """Run a complete demonstration of the trade compliance system"""
        print("🌍 INTERNATIONAL TRADE COMPLIANCE SYSTEM")
        print("=" * 50)
        
        # Display individual country information
        self.display_country_info("Italy")
        self.display_country_info("India")
        
        # Display bilateral information
        self.display_bilateral_info()
        
        # Compare countries
        self.compare_countries("Italy", "India")
        
        print(f"\n{'='*60}")
        print("DEMONSTRATION COMPLETED SUCCESSFULLY!")
        print(f"{'='*60}")

# This part makes the code run when you execute the file
if __name__ == "__main__":
    trade_system = InternationalTradeCompliance()
    trade_system.run_demo()