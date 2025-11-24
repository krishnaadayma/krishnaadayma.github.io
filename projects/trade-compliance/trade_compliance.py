#!/usr/bin/env python3
"""
trade_compliance.py

Clean, self-contained Trade Compliance module and CLI.

Replaces previous accidental HTML content stored in this file.
This script provides:
- TradeCompliance dataclass that computes:
  - import duty, tax (VAT/GST), shipping, total landed cost
  - base compliance fee and a heuristic clearance-time estimate
- Batch/demo runner to generate multiple sample reports
- CLI to calculate a single scenario and optionally export JSON/CSV
- Input validation and helpful --help usage
- No external dependencies (uses stdlib only)

Copy-paste this entire file into projects/trade-compliance/trade_compliance.py
"""

from __future__ import annotations
import argparse
import csv
import json
import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Iterable, List, Optional

# ---------------------------
# Configuration / Constants
# ---------------------------

# Example/demo duty rates keyed by (destination_country, product_category)
DUTY_RATES: Dict[tuple, float] = {
    ("italy", "textiles"): 0.10,
    ("italy", "machinery"): 0.07,
    ("italy", "pharmaceuticals"): 0.05,
    ("italy", "automotive"): 0.08,
    ("italy", "food"): 0.15,
    ("india", "textiles"): 0.08,
    ("india", "machinery"): 0.04,
    ("india", "pharmaceuticals"): 0.03,
    ("india", "automotive"): 0.06,
    ("india", "food"): 0.12,
    # fallback categories intentionally omitted; fallback handled below
}

# Example tax rates (VAT/GST) applied for imports into destination country
TAX_RATES: Dict[str, float] = {
    "italy": 0.22,  # VAT example
    "india": 0.18,  # GST example
}

CURRENCY_MAP: Dict[str, str] = {"italy": "EUR", "india": "INR"}

DEFAULT_DUTY: float = 0.05  # fallback duty rate if none specified
COMPLIANCE_FEE_RATE: float = 0.02  # 2% base compliance fee (demo)
LOG_FORMAT: str = "%(asctime)s - %(levelname)s - %(message)s"

# ---------------------------
# Utilities
# ---------------------------


def safe_round(value: float, ndigits: int = 2) -> float:
    """Round a float safely to avoid negative zero etc."""
    return round(float(value), ndigits)


def validate_non_negative(value: str) -> float:
    """argparse type: ensure float and non-negative."""
    try:
        f = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid number: {value}") from exc
    if f < 0:
        raise argparse.ArgumentTypeError(f"Value must be non-negative: {value}")
    return f


def now_iso() -> str:
    """UTC ISO timestamp (Z)"""
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


# ---------------------------
# Core Data Model
# ---------------------------


@dataclass
class TradeCompliance:
    """
    Data model for a single trade compliance calculation.

    Fields:
      - destination: country where goods are imported into (e.g., 'italy' or 'india')
      - origin: origin country string for context
      - product_category: category string; used to lookup duty rate
      - shipment_value: declared value of the shipment (numeric)
      - shipping_cost: shipping & insurance (numeric)
      - currency: currency code (optional override)
    """

    destination: str = "italy"
    origin: str = "india"
    product_category: str = "electronics"
    shipment_value: float = 0.0
    shipping_cost: float = 0.0
    currency: Optional[str] = None

    def __post_init__(self) -> None:
        self.destination = (self.destination or "italy").strip().lower()
        self.origin = (self.origin or "india").strip().lower()
        self.product_category = (self.product_category or "electronics").strip().lower()
        if self.currency is None:
            self.currency = CURRENCY_MAP.get(self.destination, "USD")

    def duty_rate(self) -> float:
        """Lookup duty rate for (destination, product_category) or return DEFAULT_DUTY."""
        return float(DUTY_RATES.get((self.destination, self.product_category), DEFAULT_DUTY))

    def tax_rate(self) -> float:
        """Lookup tax (VAT/GST) rate for destination, defaulting to 0.0 if unknown."""
        return float(TAX_RATES.get(self.destination, 0.0))

    def estimate_clearance_hours(self, import_duty: float, tax_rate: float) -> int:
        """
        Heuristic clearance time estimator (demo only).
        - base 24 hours
        - increases with duty level and tax rate and product sensitivity
        Returns integer hours.
        """
        base_hours = 24.0
        # duty as proportion of shipment value (percent)
        if self.shipment_value > 0:
            duty_pct = (import_duty / self.shipment_value) * 100.0
        else:
            duty_pct = 0.0
        base_hours += min(max(duty_pct * 0.5, 0.0), 120.0)  # scale factor
        base_hours += tax_rate * 24.0

        # category sensitivities (examples)
        if self.product_category in {"pharmaceuticals", "automotive"}:
            base_hours += 24.0
        elif self.product_category in {"machinery"}:
            base_hours += 12.0
        elif self.product_category in {"electronics"}:
            base_hours += 4.0

        # clamp to 4..240
        hours = int(max(4.0, min(base_hours, 240.0)))
        return hours

    def calculate_costs(self) -> Dict[str, Any]:
        """Compute import duty, tax, compliance fee, total landed cost and return breakdown dict."""
        sv = float(self.shipment_value or 0.0)
        sc = float(self.shipping_cost or 0.0)
        dr = self.duty_rate()
        tr = self.tax_rate()

        import_duty = sv * dr
        taxable_value = sv + import_duty + sc
        tax = taxable_value * tr
        total_landed_cost = sv + import_duty + tax + sc
        compliance_fee = sv * COMPLIANCE_FEE_RATE
        clearance_hours = self.estimate_clearance_hours(import_duty=import_duty, tax_rate=tr)

        result = {
            "timestamp": now_iso(),
            "origin": self.origin,
            "destination": self.destination,
            "product_category": self.product_category,
            "currency": self.currency,
            "shipment_value": safe_round(sv, 2),
            "shipping_cost": safe_round(sc, 2),
            "duty_rate": safe_round(dr, 4),
            "import_duty": safe_round(import_duty, 2),
            "tax_rate": safe_round(tr, 4),
            "tax": safe_round(tax, 2),
            "base_compliance_fee": safe_round(compliance_fee, 2),
            "total_landed_cost": safe_round(total_landed_cost, 2),
            "estimated_clearance_hours": clearance_hours,
        }
        return result

    def to_pretty_text(self) -> str:
        """Return a human-friendly multi-line string of the result."""
        r = self.calculate_costs()
        lines = [
            "Trade Compliance Cost Breakdown",
            "-" * 36,
            f"Origin:             {r['origin']}",
            f"Destination:        {r['destination']}",
            f"Product category:   {r['product_category']}",
            f"Currency:           {r['currency']}",
            f"Shipment value:     {r['shipment_value']:,}",
            f"Shipping cost:      {r['shipping_cost']:,}",
            f"Duty rate:          {r['duty_rate'] * 100:.2f}%",
            f"Import duty:        {r['import_duty']:,}",
            f"Tax rate:           {r['tax_rate'] * 100:.2f}%",
            f"Tax:                {r['tax']:,}",
            f"Compliance fee:     {r['base_compliance_fee']:,}",
            f"Total landed cost:  {r['total_landed_cost']:,}",
            f"Est. clearance (h): {r['estimated_clearance_hours']}h",
            "-" * 36,
        ]
        return "\n".join(lines)


# ---------------------------
# Batch / Demo helpers
# ---------------------------


def generate_demo_scenarios() -> List[TradeCompliance]:
    """Return a set of example TradeCompliance scenarios for batch runs or demos."""
    scenarios = [
        TradeCompliance(destination="italy", origin="india", product_category="textiles", shipment_value=10000, shipping_cost=500),
        TradeCompliance(destination="italy", origin="india", product_category="machinery", shipment_value=50000, shipping_cost=1500),
        TradeCompliance(destination="india", origin="italy", product_category="pharmaceuticals", shipment_value=20000, shipping_cost=800),
        TradeCompliance(destination="india", origin="italy", product_category="food", shipment_value=5000, shipping_cost=300),
        TradeCompliance(destination="italy", origin="india", product_category="electronics", shipment_value=75000, shipping_cost=2000),
    ]
    return scenarios


def export_json(path: Path, data: Any, pretty: bool = True) -> None:
    """Write JSON data to path."""
    indent = 2 if pretty else None
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=indent, ensure_ascii=False)
    logging.info("Wrote JSON to %s", path)


def export_csv(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    """Export an iterable of dicts to CSV (columns inferred from first row)."""
    rows = list(rows)
    if not rows:
        logging.warning("No rows to write to CSV: %s", path)
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    logging.info("Wrote CSV to %s", path)


# ---------------------------
# CLI
# ---------------------------


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Trade Compliance demo CLI")
    p.add_argument("--destination", "-d", choices=["italy", "india"], default="italy",
                   help="Destination country (imports into this country)")
    p.add_argument("--origin", "-o", default="india",
                   help="Origin country (context only)")
    p.add_argument("--category", "-c",
                   choices=["textiles", "machinery", "pharmaceuticals", "automotive", "food", "electronics"],
                   default="electronics", help="Product category")
    p.add_argument("--value", "-v", type=validate_non_negative, default=50000.0,
                   help="Declared shipment value (numeric)")
    p.add_argument("--shipping", "-s", type=validate_non_negative, default=500.0,
                   help="Shipping & insurance cost")
    p.add_argument("--json", action="store_true", help="Output JSON to stdout")
    p.add_argument("--csv", type=str, default=None, help="Write CSV file (batch/demo only). Provide path.")
    p.add_argument("--output", "-O", type=str, default=None, help="Write JSON output to file (path)")
    p.add_argument("--batch", action="store_true", help="Run demo batch scenarios and export results")
    p.add_argument("--pretty", action="store_true", help="Pretty-print JSON (when --json or --output used)")
    p.add_argument("--verbose", "-V", action="store_true", help="Enable verbose logging")
    return p


def cli_main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    logging.basicConfig(level=logging.INFO if not args.verbose else logging.DEBUG, format=LOG_FORMAT)

    if args.batch:
        logging.info("Running demo batch scenarios")
        scenarios = generate_demo_scenarios()
        results = [s.calculate_costs() for s in scenarios]

        # export CSV if requested
        if args.csv:
            export_csv(Path(args.csv), results)

        # export JSON if requested via --output or print to stdout via --json
        if args.output:
            export_json(Path(args.output), results, pretty=args.pretty)
        if args.json and not args.output:
            print(json.dumps(results, indent=2 if args.pretty else None, ensure_ascii=False))
        return 0

    # Single scenario run
    tc = TradeCompliance(
        destination=args.destination,
        origin=args.origin,
        product_category=args.category,
        shipment_value=float(args.value),
        shipping_cost=float(args.shipping),
    )

    if args.json:
        out = tc.calculate_costs()
        print(json.dumps(out, indent=2 if args.pretty else None, ensure_ascii=False))
        if args.output:
            export_json(Path(args.output), out, pretty=args.pretty)
    else:
        # print pretty report
        print(tc.to_pretty_text())
        if args.output:
            export_json(Path(args.output), tc.calculate_costs(), pretty=args.pretty)

    return 0


# ---------------------------
# Module test / Example runtime
# ---------------------------


def _demo_run_print() -> None:
    """Run a quick demo (used when module executed without args)."""
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    scenarios = generate_demo_scenarios()
    for s in scenarios:
        print(s.to_pretty_text())


if __name__ == "__main__":
    # If executed directly with no flags, run a demo batch and show output.
    import sys

    if len(sys.argv) == 1:
        # No CLI args -> run demo summaries
        _demo_run_print()
        raise SystemExit(0)

    raise SystemExit(cli_main())
