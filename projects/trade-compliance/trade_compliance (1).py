#!/usr/bin/env python3
"""
trade_compliance.py

Minimal, self-contained TradeCompliance module + CLI for demo and download.
- calculate costs (import duty, tax, shipping, compliance fee, total landed cost)
- estimate clearance hours (simple heuristic)
- supports single-run CLI, batch demo, JSON/CSV export
"""

from __future__ import annotations
import argparse
import csv
import json
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

# Demo rates (replace with authoritative data as needed)
DUTY_RATES: Dict[tuple, float] = {
    ("italy", "textiles"): 0.10,
    ("italy", "machinery"): 0.07,
    ("italy", "pharmaceuticals"): 0.05,
    ("italy", "automotive"): 0.08,
    ("italy", "food"): 0.15,
    ("italy", "electronics"): 0.06,
    ("india", "textiles"): 0.08,
    ("india", "machinery"): 0.04,
    ("india", "pharmaceuticals"): 0.03,
    ("india", "automotive"): 0.06,
    ("india", "food"): 0.12,
    ("india", "electronics"): 0.05,
}
TAX_RATES = {"italy": 0.22, "india": 0.18}
CURRENCY = {"italy": "EUR", "india": "INR"}
DEFAULT_DUTY = 0.05
COMPLIANCE_FEE_RATE = 0.02


def _round(v, n=2):
    return round(float(v), n)


def now_iso():
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


@dataclass
class TradeCompliance:
    destination: str = "italy"
    origin: str = "india"
    product_category: str = "electronics"
    shipment_value: float = 0.0
    shipping_cost: float = 0.0

    def __post_init__(self):
        self.destination = (self.destination or "italy").lower()
        self.origin = (self.origin or "india").lower()
        self.product_category = (self.product_category or "electronics").lower()

    def duty_rate(self) -> float:
        return float(DUTY_RATES.get((self.destination, self.product_category), DEFAULT_DUTY))

    def tax_rate(self) -> float:
        return float(TAX_RATES.get(self.destination, 0.0))

    def estimate_clearance_hours(self, import_duty: float, tax_rate: float) -> int:
        base = 24.0
        if self.shipment_value > 0:
            duty_pct = (import_duty / self.shipment_value) * 100.0
        else:
            duty_pct = 0.0
        base += min(max(duty_pct * 0.5, 0.0), 120.0)
        base += tax_rate * 24.0
        if self.product_category in ("pharmaceuticals", "automotive"):
            base += 24.0
        elif self.product_category == "machinery":
            base += 12.0
        elif self.product_category == "electronics":
            base += 4.0
        return int(max(4.0, min(base, 240.0)))

    def calculate_costs(self) -> Dict[str, Any]:
        sv = float(self.shipment_value or 0.0)
        sc = float(self.shipping_cost or 0.0)
        dr = self.duty_rate()
        tr = self.tax_rate()
        import_duty = sv * dr
        taxable = sv + import_duty + sc
        tax = taxable * tr
        compliance_fee = sv * COMPLIANCE_FEE_RATE
        total = sv + import_duty + tax + sc
        clearance = self.estimate_clearance_hours(import_duty, tr)
        return {
            "timestamp": now_iso(),
            "origin": self.origin,
            "destination": self.destination,
            "product_category": self.product_category,
            "currency": CURRENCY.get(self.destination, "USD"),
            "shipment_value": _round(sv, 2),
            "shipping_cost": _round(sc, 2),
            "duty_rate": _round(dr, 4),
            "import_duty": _round(import_duty, 2),
            "tax_rate": _round(tr, 4),
            "tax": _round(tax, 2),
            "base_compliance_fee": _round(compliance_fee, 2),
            "total_landed_cost": _round(total, 2),
            "estimated_clearance_hours": clearance,
        }

    def to_pretty(self) -> str:
        d = self.calculate_costs()
        lines = [
            "Trade Compliance Cost Breakdown",
            "----------------------------------------",
            f"Origin:             {d['origin']}",
            f"Destination:        {d['destination']}",
            f"Product category:   {d['product_category']}",
            f"Currency:           {d['currency']}",
            f"Shipment value:     {d['shipment_value']:,}",
            f"Shipping cost:      {d['shipping_cost']:,}",
            f"Duty rate:          {d['duty_rate']*100:.2f}%",
            f"Import duty:        {d['import_duty']:,}",
            f"Tax rate:           {d['tax_rate']*100:.2f}%",
            f"Tax:                {d['tax']:,}",
            f"Compliance fee:     {d['base_compliance_fee']:,}",
            f"Total landed cost:  {d['total_landed_cost']:,}",
            f"Est. clearance (h): {d['estimated_clearance_hours']}",
            "----------------------------------------",
        ]
        return "\n".join(lines)


def generate_demo() -> List[Dict[str, Any]]:
    scenarios = [
        TradeCompliance("italy", "india", "textiles", 10000, 500),
        TradeCompliance("italy", "india", "machinery", 50000, 1500),
        TradeCompliance("india", "italy", "pharmaceuticals", 20000, 800),
    ]
    return [s.calculate_costs() for s in scenarios]


def write_json(path: Path, data: Any, pretty: bool = True):
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2 if pretty else None, ensure_ascii=False)


def write_csv(path: Path, rows: List[Dict[str, Any]]):
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def build_parser():
    p = argparse.ArgumentParser(description="Trade Compliance CLI")
    p.add_argument("--destination", "-d", choices=["italy", "india"], default="italy")
    p.add_argument("--origin", "-o", default="india")
    p.add_argument("--category", "-c", choices=["textiles", "machinery", "pharmaceuticals", "automotive", "food", "electronics"], default="electronics")
    p.add_argument("--value", "-v", type=float, default=50000.0)
    p.add_argument("--shipping", "-s", type=float, default=500.0)
    p.add_argument("--json", action="store_true", help="print JSON to stdout")
    p.add_argument("--output", "-O", type=str, help="write JSON to file")
    p.add_argument("--csv", type=str, help="write batch CSV")
    p.add_argument("--batch", action="store_true", help="run demo batch")
    return p


def main(argv=None):
    p = build_parser()
    args = p.parse_args(argv)
    if args.batch:
        rows = generate_demo()
        if args.csv:
            write_csv(Path(args.csv), rows)
            print(f"Wrote CSV to {args.csv}")
        if args.output:
            write_json(Path(args.output), rows)
            print(f"Wrote JSON to {args.output}")
        if args.json and not args.output:
            print(json.dumps(rows, indent=2))
        return 0

    tc = TradeCompliance(args.destination, args.origin, args.category, args.value, args.shipping)
    if args.json:
        print(json.dumps(tc.calculate_costs(), indent=2))
    else:
        print(tc.to_pretty())
    if args.output:
        write_json(Path(args.output), tc.calculate_costs())
        print(f"Wrote JSON to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
