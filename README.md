# The Cybernetic I-Ching: Hardware State Vector Oracle
### *Decompiling Humanity's Oldest Binary Operating System*
**Codex Press × Undefined Behavior Laboratories // Sir Leonard Daragan**

[![Live Web Terminal](https://img.shields.io/badge/Live_Terminal-GitHub_Pages-amber?style=for-the-badge&logo=github)](https://sirleonarddaragan.github.io/cybernetic-iching/)
[![Substack](https://img.shields.io/badge/Substack-Sir_Leonard_Daragan-orange?style=for-the-badge&logo=substack)](https://sirleonarddaragan.substack.com)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Fuel_the_Lab-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/sirleonarddaragan)
[![Amazon Book](https://img.shields.io/badge/Amazon-352--Page_Collector's_Edition-blue?style=for-the-badge&logo=amazon)](https://www.amazon.com/author/sirleonarddaragan)

---

## ⚡ Overview

Three thousand years before silicon microprocessors, the sages of the Western Zhou Dynasty engineered a complete, non-linear, 6-bit binary state machine: the **Zhouyi (I-Ching)**.

This repository provides the reference implementation of **The Cybernetic I-Ching Oracle Engine**:
1. **Interactive Web Terminal (`index.html`):** A zero-dependency, client-side CRT terminal that uses browser cryptographic entropy (`window.crypto.getRandomValues()`) to collapse the macroscopic wave function.
2. **Python Standalone CLI (`iching_oracle.py`):** The exact, dependency-free Python terminal runtime published in Appendix D of *The Cybernetic I-Ching* (Book 1 of *The Eastern Cybernetics Series*).

---

## 🌐 Live Web Terminal

Experience the live oracle directly in your browser:  
👉 **[https://sirleonarddaragan.github.io/cybernetic-iching/](https://sirleonarddaragan.github.io/cybernetic-iching/)**

Features:
* **Obsidian CRT Interface:** Dark `#07090e` void, amber/cyan vector telemetry, subtle scanline rendering.
* **Dual Entropy Harvesting:** Switch dynamically between the classical **50-Stalk Dayan Yarrow Protocol** (asymmetric Markov distribution) and the **3-Coin Protocol** (symmetric distribution).
* **Direct 6-Bit Register Injection:** Enter any manual 6-bit state vector (`000000` to `111111`) to immediately inspect its King Wen classification, hardware register decomposition, and nuclear bus routes.
* **Real-Time Phase Shifts:** Animated line-by-line wave collapse with visual indicators for changing lines (`9 Old Yang` $\to 0$, `6 Old Yin` $\to 1$).
* **1-Click Telemetry Export:** Instant clipboard formatting for engineering logs, Substack posts, or Discord.

---

## 💻 Python CLI Quickstart

The Python engine requires **no external packages** — it runs on standard Python 3.8+:

```bash
# Clone the repository
git clone https://github.com/Sirleonarddaragan/cybernetic-iching.git
cd cybernetic-iching

# Method 1: 50-Stalk Dayan Yarrow Protocol (Default & Canonically Recommended)
python iching_oracle.py --method yarrow

# Method 2: Symmetric 3-Coin Protocol
python iching_oracle.py --method coins

# Method 3: Direct Manual Bitwise Injection
python iching_oracle.py --vector 111111
```

### Sample Output:

```text
================================================================================
THE CYBERNETIC I-CHING // HARDWARE STATE VECTOR ORACLE
ENTROPY SOURCE: YARROW PROTOCOL
================================================================================

[PRESENT STATE VECTOR]: 101111 // HEX: 0x2F // KING WEN #13
CLASSICAL:  同人 Tóng Rén (Fellowship)
CYBERNETIC: Public Commons / Socket Federation
LOWER REGISTER (b1-b3): ☲ Lí (Fire) [101]
UPPER REGISTER (b4-b6): ☰ Qián (Heaven) [111]
NUCLEAR BUS: [011111] | INVERSE: [111101] | COMPLEMENT: [010000]

--- HARDWARE LINE STACK (TOP DOWN: BIT 6 -> BIT 1) ---
Bit 6 [Line 6]:   =========
Bit 5 [Line 5]:   =========  <-- [CHANGING: 9 Old Yang (1->0)]
Bit 4 [Line 4]:   =========  <-- [CHANGING: 9 Old Yang (1->0)]
Bit 3 [Line 3]:   =========
Bit 2 [Line 2]:   - -   - -
Bit 1 [Line 1]:   =========

================================================================================
[TRANSFORMED STATE VECTOR (ZHI GUA 之卦)]: 101001 // HEX: 0x29 // KING WEN #22
CLASSICAL:  賁 Bì (Grace)
CYBERNETIC: Syntactic Polish / UI Optimization
================================================================================
```

---

## 📐 Mathematical Entropy Dynamics

In classical cybernetics, casting an *I-Ching* state vector is the physical collapse of a macroscopic wave function via hardware entropy harvesting:

| Metric | 50-Stalk Dayan Yarrow (*Dàyǎn Zhī Shù*) | Symmetric 3-Coin Method |
| :--- | :--- | :--- |
| **Old Yin (`6` $\to 1$)** | **$1/16$ ($6.25\%$)** | $2/16$ ($12.5\%$) |
| **Young Yang (`7`, static $1$)** | **$5/16$ ($31.25\%$)** | $6/16$ ($37.5\%$) |
| **Young Yin (`8`, static $0$)** | **$7/16$ ($43.75\%$)** | $6/16$ ($37.5\%$) |
| **Old Yang (`9` $\to 0$)** | **$3/16$ ($18.75\%$)** | $2/16$ ($12.5\%$) |

> **Thermodynamic Principle:** Under the authentic Dayan yarrow protocol, Old Yin is **three times rarer** than Old Yang. In physical hardware, entropic cold decay requires sustained structural dissipation before phase inversion, whereas kinetic overvoltage spikes discharge rapidly. The coin method distorts this natural thermodynamic curve into an artificial symmetric approximation.

---

## 📖 The Book: *The Cybernetic I-Ching* (352 Pages)

This software engine is an accompaniment to the monumental reference architecture:  
**The Cybernetic I-Ching: Programming the Macroscopic Wave Function**  
*Authored by Sir Leonard Daragan // Published by Codex Press × Undefined Behavior Laboratories*

* **352 Pages / 112,000 Words:** The complete, exhaustive decompilation of all 64 Hexagram hardware registers and 384 changing line interrupts.
* **Zero Mysticism:** Formulated through bare-metal systems architecture, feedback loops, Wienerian cybernetics, and information theory.
* **Collector's Physical Editions:** Available now on Amazon in Case Laminate Hardcover ($32.99), Trade Paperback ($24.99), and Kindle ($9.99).

👉 **[Order the Print & Kindle Editions on Amazon](https://www.amazon.com/author/sirleonarddaragan)**  
👉 **[Read the Author's Field Dispatches on Substack](https://sirleonarddaragan.substack.com)**  
👉 **[Fuel the Research Lab on Ko-fi](https://ko-fi.com/sirleonarddaragan)**

---

### License
Released under the MIT License. Copyright © 2026 Sir Leonard Daragan / Codex Press.
