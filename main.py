#!/usr/bin/env python3
"""
PASSWORD CRACKING & CREDENTIAL ATTACK SUITE
Ethical Password Security Toolkit

Main entry point – orchestrates all modules.
Educational use only. Always obtain proper authorization.
"""

import argparse
import os
import sys
from datetime import datetime

# Ensure modules can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules.dictionary_generator import DictionaryGenerator
from modules.hash_extractor import HashExtractor
from modules.brute_force_simulator import BruteForceSimulator
from modules.strength_analyzer import StrengthAnalyzer
from modules.report_generator import ReportGenerator


BANNER = r"""
╔══════════════════════════════════════════════════════════════════╗
║     PASSWORD CRACKING & CREDENTIAL ATTACK SUITE                  ║
║           Ethical Password Security Toolkit                      ║
╚══════════════════════════════════════════════════════════════════╝
"""


def print_banner():
    print(BANNER)
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)


def run_dictionary_generator(args):
    print("\n[ MODULE ] Dictionary Generator\n")
    dg = DictionaryGenerator()

    if args.demo or getattr(args, 'full', False):
        dg.generate_demo_wordlist()
        return

    print("1. Add common passwords")
    print("2. Add keyboard patterns")
    print("3. Add name+year patterns")
    print("4. Apply mutations to words")
    print("5. Generate hybrid combinations")
    print("6. All of the above (full wordlist)")
    choice = input("\nSelect option (1-6): ").strip()

    if choice == "1":
        dg.add_common_passwords()
    elif choice == "2":
        dg.add_keyboard_patterns()
    elif choice == "3":
        names = input("Enter names (comma-separated): ").strip().split(",")
        names = [n.strip() for n in names if n.strip()]
        dg.add_name_year_patterns(names)
    elif choice == "4":
        words = input("Enter base words (comma-separated): ").strip().split(",")
        words = [w.strip() for w in words if w.strip()]
        dg.apply_mutations(words)
    elif choice == "5":
        list_a = input("List A (comma-separated): ").strip().split(",")
        list_b = input("List B (comma-separated): ").strip().split(",")
        dg.add_hybrid_combinations(
            [x.strip() for x in list_a if x.strip()],
            [x.strip() for x in list_b if x.strip()]
        )
    elif choice == "6":
        dg.generate_demo_wordlist()
        return
    else:
        print("[!] Invalid choice")
        return

    filename = input("Output filename [custom_wordlist.txt]: ").strip() or "custom_wordlist.txt"
    dg.save_wordlist(filename)


def run_hash_extractor(args):
    print("\n[ MODULE ] Hash Extractor\n")
    he = HashExtractor()
    he.extract_shadow_file()
    he.extract_sam_file()
    he.print_summary()
    he.save_hashes()


def run_brute_force_simulator(args):
    print("\n[ MODULE ] Brute-Force Simulator\n")
    bfs = BruteForceSimulator()
    bfs.run_demo_simulations()
    bfs.save_results()


def run_strength_analyzer(args):
    print("\n[ MODULE ] Password Strength Analyzer\n")
    sa = StrengthAnalyzer()
    sa.run_demo_analysis()
    sa.save_analysis()


def run_full_pipeline(args):
    print("\nRunning all modules in DEMO mode...\n")
    print("=" * 70)
    print(" RUNNING FULL AUDIT PIPELINE")
    print("=" * 70)

    # 1. Dictionary
    print("\n[1/5] Generating Dictionary...")
    dg = DictionaryGenerator()
    wordlist_path = dg.generate_demo_wordlist()

    # 2. Hash extraction
    print("\n[2/5] Extracting Hashes...")
    he = HashExtractor()
    he.extract_shadow_file()
    he.extract_sam_file()
    he.print_summary()
    hash_path = he.save_hashes()

    # 3. Brute-force simulations
    print("\n[3/5] Running Brute-Force Simulations...")
    bfs = BruteForceSimulator()
    # Load wordlist size for info
    try:
        with open(wordlist_path) as f:
            word_count = sum(1 for _ in f)
        print(f"[+] Loaded {word_count} words from {wordlist_path}")
    except Exception:
        pass
    sim_results = bfs.run_demo_simulations()
    sim_path = bfs.save_results()

    # 4. Strength analysis
    print("\n[4/5] Analyzing Password Strength...")
    sa = StrengthAnalyzer()
    analyses = sa.run_demo_analysis()
    analysis_path = sa.save_analysis()

    # 5. Audit report
    print("\n[5/5] Generating Audit Report...")
    rg = ReportGenerator()
    rg.add_strength_analyses(analyses)
    rg.add_simulation_results(sim_results)
    rg.add_hash_data(he.extracted_hashes)
    rg.add_wordlist_info({
        "path": wordlist_path,
        "unique_entries": len(dg.wordlist)
    })
    report_path = rg.save_report()

    print("\n" + "=" * 70)
    print(" PIPELINE COMPLETE – OUTPUT FILES")
    print("=" * 70)
    print(f"  Wordlist      : {wordlist_path}")
    print(f"  Hashes        : {hash_path}")
    print(f"  Simulations   : {sim_path}")
    print(f"  Analysis      : {analysis_path}")
    print(f"  Audit Report  : {report_path}")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Password Cracking & Credential Attack Suite – Ethical Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 main.py --demo
  python3 main.py --module dict
  python3 main.py --module full
  python3 main.py --interactive
        """
    )
    parser.add_argument("--demo", action="store_true", help="Run full pipeline in demo mode")
    parser.add_argument("--module", choices=["dict", "hash", "brute", "strength", "report", "full"],
                        help="Run a specific module")
    parser.add_argument("--interactive", action="store_true", help="Interactive module selection")

    args = parser.parse_args()
    print_banner()

    if args.demo:
        print("\n  Running all modules in DEMO mode...\n")
        run_full_pipeline(args)
    elif args.module == "dict":
        run_dictionary_generator(args)
    elif args.module == "hash":
        run_hash_extractor(args)
    elif args.module == "brute":
        run_brute_force_simulator(args)
    elif args.module == "strength":
        run_strength_analyzer(args)
    elif args.module == "report":
        print("\n[ MODULE ] Report Generator\n")
        print("Run full pipeline first with: python3 main.py --module full")
    elif args.module == "full":
        run_full_pipeline(args)
    elif args.interactive:
        print("\n  Interactive mode – select modules to run:\n")
        print("  1. Dictionary Generator")
        print("  2. Hash Extractor")
        print("  3. Brute-Force Simulator")
        print("  4. Password Strength Analyzer")
        print("  5. Full Pipeline (all modules)")
        choice = input("\nSelect option (1-5): ").strip()
        module_map = {
            "1": "dict", "2": "hash", "3": "brute",
            "4": "strength", "5": "full"
        }
        if choice in module_map:
            args.module = module_map[choice]
            if args.module == "full":
                run_full_pipeline(args)
            else:
                run_func = {
                    "dict": run_dictionary_generator,
                    "hash": run_hash_extractor,
                    "brute": run_brute_force_simulator,
                    "strength": run_strength_analyzer,
                }[args.module]
                run_func(args)
        else:
            print("[!] Invalid selection")
    else:
        parser.print_help()
        print("\nTip: Start with  python3 main.py --demo")


if __name__ == "__main__":
    main()
