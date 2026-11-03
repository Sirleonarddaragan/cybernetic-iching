#!/usr/bin/env python3
"""
THE CYBERNETIC I-CHING: TERMINAL ORACLE CLI
Codex Press × Undefined Behavior Laboratories // Sir Leonard Daragan
Hardware Vector Compilation & Macroscopic Wave Function Collapser

Usage:
    python iching_oracle.py --method yarrow
    python iching_oracle.py --method coins
    python iching_oracle.py --vector 111011
"""

import sys
import random
import argparse

# Cross-platform UTF-8 terminal encoding
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Ensure UTF-8 output encoding across Windows/Linux/macOS terminal environments
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# 64-Hexagram Canonical Lookup Registry (Vector bottom-to-top -> (KW#, Name, Class))
HEXAGRAM_REGISTRY = {
    "111111": (1, "乾 Qián (The Creative)", "Master Voltage Rail / Pure Kernel"),
    "000000": (2, "坤 Kūn (The Receptive)", "Zero-Ground Chassis / RAM Pool"),
    "100010": (3, "屯 Zhūn (Birth Throes)", "High-Entropy Boot / Cold Init"),
    "010001": (4, "蒙 Méng (Youthful Folly)", "Uncalibrated Heuristics / Sandbox"),
    "111010": (5, "需 Xū (Waiting)", "Waiting Buffer / Paced Clock"),
    "010111": (6, "訟 Sòng (Conflict)", "Resource Arbitration / Contention"),
    "010000": (7, "師 Shī (The Army)", "Coordinated Daemon Swarm"),
    "000010": (8, "比 Bǐ (Holding Together)", "P2P Consensus / Mesh Federation"),
    "111011": (9, "小畜 Xiǎo Xù (Small Taming)", "Micro-Buffering / Latent Charge"),
    "110111": (10, "履 Lǚ (Treading)", "Privileged Kernel Protocol"),
    "111000": (11, "泰 Tài (Peace)", "Full-Duplex Homeostasis"),
    "000111": (12, "否 Pǐ (Standstill)", "Total Bus Disconnection / Deadlock"),
    "101111": (13, "同人 Tóng Rén (Fellowship)", "Public Commons / Socket Federation"),
    "111101": (14, "大有 Dà Yǒu (Great Possession)", "Supercomputing Cluster Allocation"),
    "001000": (15, "謙 Qiān (Modesty)", "Zero-Ground Impedance Reference"),
    "000100": (16, "豫 Yù (Enthusiasm)", "Resonance Cascade / Phase Lock"),
    "100110": (17, "隨 Suí (Following)", "Dynamic Feedback Tracking (PLL)"),
    "011001": (18, "蠱 Gǔ (Work on Decay)", "Poisoned Cache Invalidation / Repair"),
    "110000": (19, "臨 Lín (Approach)", "Supervisory Control / Heading at Scale"),
    "000011": (20, "觀 Guān (Contemplation)", "Passive Observability & Telemetry"),
    "100101": (21, "噬嗑 Shì Kè (Biting Through)", "Hardware Mutex Purge / Arbitration"),
    "101001": (22, "賁 Bì (Grace)", "Syntactic Polish / UI Optimization"),
    "000001": (23, "剝 Bō (Splitting Apart)", "Systemic Decay / Graceful Degradation"),
    "100000": (24, "復 Fù (Return)", "Cold Reboot / Solstice Reset Bit"),
    "100111": (25, "无妄 Wú Wàng (Innocence)", "Zero-Exploit Integrity / Spontaneity"),
    "111001": (26, "大畜 Dà Xù (Great Taming)", "High-Capacity Buffer Storage"),
    "100001": (27, "頤 Yí (Nourishment)", "I/O Channel Calibration & Intake"),
    "011110": (28, "大過 Dà Guò (Critical Load)", "Structural Criticality / Beam Deflection"),
    "010010": (29, "坎 Kǎn (The Abysmal)", "Recursive Chasm / Threat Modeling"),
    "101101": (30, "離 Lí (The Clinging)", "Radiant Telemetry / Optical Bus"),
    "001110": (31, "咸 Xián (Mutual Attraction)", "Magnetic Inductive Coupling / Field"),
    "011100": (32, "恆 Héng (Duration)", "Daemon Persistence / Gyro Invariance"),
    "001111": (33, "遯 Dùn (Retreat)", "Strategic Decoupling / Anonymization"),
    "111100": (34, "大壯 Dà Zhuàng (Great Power)", "Voltage Overdrive / Kinetic Surge"),
    "000101": (35, "晉 Jìn (Progress)", "Daylight Ingress / Bandwidth Growth"),
    "101000": (36, "明夷 Míng Yí (Darkening of Light)", "Zero-Knowledge Cloak / Stealth Mode"),
    "101011": (37, "家人 Jiā Rén (The Family)", "Domestic Micro-Service Topology"),
    "110101": (38, "睽 Kuí (Opposition)", "Polarity Inversion / Cross-Adapter"),
    "001010": (39, "蹇 Jiǎn (Obstruction)", "Impasse Bypass / Adaptive Routing"),
    "010100": (40, "解 Xiè (Deliverance)", "Tension Dissolution / Buffer Flush"),
    "110001": (41, "損 Sǔn (Decrease)", "Down-Throttling / Sacrificial Pruning"),
    "100011": (42, "益 Yì (Increase)", "Burst Capacity / Dynamic Expansion"),
    "111110": (43, "夬 Guài (Breakthrough)", "Privilege Revocation / Exploit Flush"),
    "011111": (44, "姤 Gòu (Coming to Meet)", "Zero-Day Seduction / Unvetted Pin"),
    "000110": (45, "萃 Cuì (Gathering Together)", "Distributed Clustering / Aggregation"),
    "011000": (46, "升 Shēng (Pushing Upward)", "Vertical Scaling / Substrate Accretion"),
    "010110": (47, "困 Kùn (Exhaustion)", "Resource Starvation / Sandbox Lock"),
    "011010": (48, "井 Jǐng (The Well)", "Substrate Reservoir / Immutable Well"),
    "101110": (49, "革 Gé (Revolution)", "Radical Hard Fork / Consensus Molting"),
    "011101": (50, "鼎 Dǐng (The Caldron)", "System Compiler / Vessel Alchemy"),
    "100100": (51, "震 Zhèn (The Shocking)", "Recursive Hardware IRQ / Shockwave"),
    "001001": (52, "艮 Gèn (Keeping Still)", "Hardware Mutex / Memory Barrier"),
    "001011": (53, "漸 Jiàn (Gradual Development)", "Paced Assembly / Stepwise Ingress"),
    "110100": (54, "歸妹 Guī Mèi (The Marrying Maiden)", "Subordinate Out-of-Order Execution"),
    "101100": (55, "豐 Fēng (Abundance)", "Peak Zenith Concurrency / Eclipse"),
    "001101": (56, "旅 Lǚ (The Wanderer)", "Transient Routing / Ephemeral Node"),
    "011011": (57, "巽 Xùn (The Gentle)", "Daemon Sub-Bus Penetration"),
    "110110": (58, "兌 Duì (The Joyous)", "Open Socket Ingress / Peer Duplex"),
    "010011": (59, "渙 Huàn (Dispersion)", "Silo Dissolution / Buffer Dispersion"),
    "110010": (60, "節 Jié (Limitation)", "Packet Pacing / Clock Division"),
    "110011": (61, "中孚 Zhōng Fú (Inner Truth)", "Zero-Knowledge Proof / Inner Truth"),
    "001100": (62, "小過 Xiǎo Guò (Small Preponderance)", "Low-Flying Telemetry / Micro-Margining"),
    "101010": (63, "既濟 Jì Jì (After Completion)", "Full System Parity / Entropic Drift"),
    "010101": (64, "未濟 Wèi Jì (Before Completion)", "Infinite Runtime Loop / Cosmic Init")
}

TRIGRAM_NAMES = {
    "111": "☰ Qián (Heaven)", "000": "☷ Kūn (Earth)",
    "100": "☳ Zhèn (Thunder)", "010": "☵ Kǎn (Water)",
    "001": "☶ Gèn (Mountain)", "011": "☴ Xùn (Wind)",
    "101": "☲ Lí (Fire)",       "110": "☱ Duì (Lake)"
}

def harvest_line_coins():
    # Symmetric 3-coin flip (Heads=3, Tails=2)
    flips = [random.choice([2, 3]) for _ in range(3)]
    return sum(flips)

def harvest_line_yarrow():
    # Asymmetric Dayan Zhi Shu: P(6)=1/16, P(7)=5/16, P(8)=7/16, P(9)=3/16
    r = random.randint(1, 16)
    if r == 1:
        return 6
    elif r <= 6:
        return 7
    elif r <= 13:
        return 8
    else:
        return 9

def render_ascii_line(bit_val, changing=False, old_val=None):
    if bit_val == '1':
        glyph = "========="
    else:
        glyph = "- -   - -"
    
    if changing:
        tag = f"  <-- [CHANGING: {'9 Old Yang (1->0)' if old_val==9 else '6 Old Yin (0->1)'}]"
    else:
        tag = ""
    return f"  {glyph}{tag}"

def run_oracle(method="yarrow", manual_vector=None):
    print("=" * 80)
    print("THE CYBERNETIC I-CHING // HARDWARE STATE VECTOR ORACLE")
    print(f"ENTROPY SOURCE: {method.upper()} PROTOCOL")
    print("=" * 80)

    if manual_vector:
        if len(manual_vector) != 6 or not all(c in '01' for c in manual_vector):
            print(f"[!] Invalid vector: '{manual_vector}'. Must be exactly 6 binary digits ('0' or '1').")
            return
        vector_str = manual_vector
        raw_vals = [7 if b == '1' else 8 for b in manual_vector]
        changed_vector = None
        has_changing = False
    else:
        raw_vals = []
        base_bits = []
        target_bits = []
        has_changing = False

        for i in range(6):
            val = harvest_line_yarrow() if method == "yarrow" else harvest_line_coins()
            raw_vals.append(val)
            if val == 6:
                base_bits.append('0')
                target_bits.append('1')
                has_changing = True
            elif val == 7:
                base_bits.append('1')
                target_bits.append('1')
            elif val == 8:
                base_bits.append('0')
                target_bits.append('0')
            elif val == 9:
                base_bits.append('1')
                target_bits.append('0')
                has_changing = True
        
        vector_str = "".join(base_bits)
        changed_vector = "".join(target_bits) if has_changing else None

    # Decompose Registers
    lower_tri = vector_str[0:3]
    upper_tri = vector_str[3:6]
    nuc_lower = vector_str[1:4]
    nuc_upper = vector_str[2:5]
    nuc_vector = nuc_lower + nuc_upper
    inv_vector = vector_str[::-1]
    comp_vector = "".join('1' if b == '0' else '0' for b in vector_str)

    kw_num, name, desc = HEXAGRAM_REGISTRY.get(vector_str, ("??", "Unknown", "Unregistered"))
    hex_addr = f"0x{int(vector_str, 2):02X}"

    print(f"\n[PRESENT STATE VECTOR]: {vector_str} // HEX: {hex_addr} // KING WEN #{kw_num:02d}")
    print(f"CLASSICAL:  {name}")
    print(f"CYBERNETIC: {desc}")
    print(f"LOWER REGISTER (b1-b3): {TRIGRAM_NAMES.get(lower_tri, 'Unknown')} [{lower_tri}]")
    print(f"UPPER REGISTER (b4-b6): {TRIGRAM_NAMES.get(upper_tri, 'Unknown')} [{upper_tri}]")
    print(f"NUCLEAR BUS: [{nuc_vector}] | INVERSE: [{inv_vector}] | COMPLEMENT: [{comp_vector}]")
    print("\n--- HARDWARE LINE STACK (TOP DOWN: BIT 6 -> BIT 1) ---")
    
    for i in reversed(range(6)):
        val = raw_vals[i]
        is_changing = val in (6, 9)
        bit = vector_str[i]
        print(f"Bit {i+1} [Line {i+1}]: {render_ascii_line(bit, is_changing, val)}")

    if has_changing and changed_vector:
        t_kw, t_name, t_desc = HEXAGRAM_REGISTRY.get(changed_vector, ("??", "Unknown", "Unregistered"))
        t_hex = f"0x{int(changed_vector, 2):02X}"
        print("\n" + "=" * 80)
        print(f"[TRANSFORMED STATE VECTOR (ZHI GUA 之卦)]: {changed_vector} // HEX: {t_hex} // KING WEN #{t_kw:02d}")
        print(f"CLASSICAL:  {t_name}")
        print(f"CYBERNETIC: {t_desc}")
        print("\n--- MUTATED HARDWARE LINE STACK (AFTER PHASE SHIFT) ---")
        for i in reversed(range(6)):
            t_bit = changed_vector[i]
            was_changing = raw_vals[i] in (6, 9)
            tag = "  <-- [MUTATED BIT]" if was_changing else ""
            glyph = "=========" if t_bit == '1' else "- -   - -"
            print(f"Bit {i+1} [Line {i+1}]:   {glyph}{tag}")
        print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The Cybernetic I-Ching Oracle CLI")
    parser.add_argument("--method", choices=["yarrow", "coins"], default="yarrow", help="Entropy harvesting method")
    parser.add_argument("--vector", type=str, default=None, help="Direct 6-bit vector (e.g. 111011)")
    args = parser.parse_args()
    run_oracle(method=args.method, manual_vector=args.vector)
