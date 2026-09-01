r"""
Video 259: Euler's Theorem and RSA -- Number Theory

Euler's theorem proof (group-theoretic), exponent reduction corollary,
RSA key generation, encryption/decryption, proof of correctness,
and a worked small-number example.

Follows v2 template quality rules.
"""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video259_EulersTheoremRSA(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_proof()
        self.scene3_exponent_reduction()
        self.scene4_rsa_setup()
        self.scene5_rsa_encrypt_decrypt()
        self.scene6_rsa_proof()
        self.scene7_worked_example()
        self.scene8_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Last time we defined Euler's totient function and stated "
            "Euler's theorem. Today we prove it and then do something "
            "remarkable. We will see how this pure result in number "
            "theory is the foundation of RSA encryption, which secures "
            "your internet browsing every single day.",
            duration=22,
        )
        play_intro(self, "Euler's Theorem and RSA", "Number Theory")
        title = self.ly.title("From Pure Math to Cryptography")
        items = [
            Text("Euler's theorem: a^phi(n) = 1 (mod n)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("This result secures your internet browsing",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_proof(self):
        self.add_subcaption(
            "Euler's theorem states: if the greatest common divisor of "
            "a and n is one, then a to the phi of n equals one mod n. "
            "The proof is elegant. The set of integers coprime to n, "
            "taken modulo n, forms a group under multiplication. "
            "Multiplying every element by a just permutes the group. "
            "Therefore the product of all elements is unchanged, and "
            "cancelling gives a to the phi of n equals one.",
            duration=36,
        )
        self.ly.section_divider(1, "Euler's Theorem")
        title = self.ly.title("Proof of Euler's Theorem")
        thm = MathTex(
            r"\gcd(a,n)=1 \; \Longrightarrow \; a^{\varphi(n)} \equiv 1 \pmod{n}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(thm, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(thm), run_time=NORMAL)
        self.wait(FAST)
        items = [
            Text("Step 1: Coprime residues mod n form a group",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Step 2: Multiplying by a permutes the group",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Step 3: Product of all elements is unchanged",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Step 4: Cancel product, get a^phi(n) = 1",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene3_exponent_reduction(self):
        self.add_subcaption(
            "A crucial corollary. Since a to the phi of n equals one, "
            "any power of a can be reduced. Specifically, a to the k "
            "equals a to the k mod phi of n, all modulo n. For example, "
            "seven to the one hundredth mod fifteen. Phi of fifteen is "
            "eight, so one hundred mod eight is four. Seven to the "
            "fourth is twenty four hundred one, which is one mod fifteen.",
            duration=34,
        )
        self.ly.section_divider(2, "Exponent Reduction")
        title = self.ly.title("Exponents Wrap Around mod phi(n)")
        cor = MathTex(
            r"a^{\varphi(n)} \equiv 1 \; \Rightarrow \; a^{k} \equiv a^{k \bmod \varphi(n)} \pmod{n}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(cor, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(cor), run_time=NORMAL)
        self.wait(FAST)
        items = [
            Text("Example: 7^100 mod 15",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("phi(15) = 8, so 100 mod 8 = 4",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("7^4 = 2401 = 1 (mod 15)  Confirmed!",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene4_rsa_setup(self):
        self.add_subcaption(
            "Now for the payoff. RSA was invented in nineteen seventy "
            "seven by Rivest, Shamir, and Adleman. First, choose two "
            "large primes p and q. Compute n equals p times q, and "
            "phi of n equals p minus one times q minus one. Then choose "
            "an encryption exponent e coprime to phi of n, and compute "
            "the decryption exponent d as the inverse of e mod phi of n.",
            duration=36,
        )
        self.ly.section_divider(3, "RSA Key Generation")
        title = self.ly.title("Setting Up RSA")
        items = [
            Text("1. Choose two large primes p, q",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. n = p*q,  phi(n) = (p-1)(q-1)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Choose e with gcd(e, phi(n)) = 1",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("4. Compute d = inverse of e (mod phi(n))",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()
        title2 = self.ly.title("Public Key vs Private Key")
        pub = Text("Public key: (e, n)  --  share with everyone",
                    font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        priv = Text("Private key: (d, n)  --  keep secret!",
                     font_size=BODY_SIZE, color=RED, font=SANS)
        self.ly.progressive_reveal([pub, priv], start_from=title2)
        self.ly.clear()

    def scene5_rsa_encrypt_decrypt(self):
        self.add_subcaption(
            "Encryption is simple. To send a message m, compute "
            "c equals m to the e mod n. This ciphertext c is what "
            "you transmit. To decrypt, the receiver computes m "
            "equals c to the d mod n, recovering the original message. "
            "Security relies on the fact that factoring n into p "
            "times q is computationally infeasible for large n.",
            duration=32,
        )
        self.ly.section_divider(4, "Encryption and Decryption")
        title = self.ly.title("The RSA Operations")
        enc = MathTex(r"c = m^{e} \pmod{n} \;\; \text{(encrypt)}",
                       font_size=HEADING_SIZE, color=PRIMARY)
        dec = MathTex(r"m = c^{d} \pmod{n} \;\; \text{(decrypt)}",
                       font_size=HEADING_SIZE, color=SECONDARY)
        self.ly.safe_place(enc, DOWN, anchor=title, buff=0.5)
        self.play(Write(enc), run_time=NORMAL)
        self.wait(FAST)
        self.ly.safe_place(dec, DOWN, anchor=enc, buff=0.4)
        self.play(Write(dec), run_time=NORMAL)
        self.wait(FAST)
        items = [
            Text("Security: factoring n = p*q is very hard",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("But knowing p, q makes phi(n) easy",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=dec)
        self.ly.clear()

    def scene6_rsa_proof(self):
        self.add_subcaption(
            "Why does decryption reverse encryption? We need to show "
            "that m to the e d equals m mod n. Since e d equals one "
            "mod phi of n, we can write e d as one plus k times phi of n "
            "for some integer k. So m to the e d equals m to the one "
            "plus k phi of n, which equals m times m to the phi of n, "
            "all to the power k. By Euler's theorem this is m times one "
            "to the k, which equals m. Done.",
            duration=42,
        )
        self.ly.section_divider(5, "Why RSA Works")
        title = self.ly.title("Proof of Correctness")
        items = [
            MathTex(r"ed \equiv 1 \pmod{\varphi(n)}",
                    font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"\Rightarrow \; ed = 1 + k\varphi(n)",
                    font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"m^{ed} = m^{1 + k\varphi(n)} = m \cdot (m^{\varphi(n)})^{k}",
                    font_size=BODY_SIZE, color=WHITE),
            MathTex(r"= m \cdot 1^{k} = m \pmod{n} \; \checkmark",
                    font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene7_worked_example(self):
        self.add_subcaption(
            "Let's walk through a tiny RSA example. Choose p equals "
            "three, q equals eleven. Then n equals thirty three, and "
            "phi of n equals twenty. Choose e equals three, which is "
            "coprime to twenty. The inverse of three mod twenty is "
            "seven, since three times seven is twenty one, which is one "
            "mod twenty. Now encrypt the message fourteen.",
            duration=34,
        )
        self.ly.section_divider(6, "Worked Example")
        title = self.ly.title("Tiny RSA: p=3, q=11")
        items = [
            Text("n = 3*11 = 33,  phi(33) = 2*10 = 20",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("e = 3,  d = 7  (since 3*7 = 21 = 1 mod 20)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Encrypt: 14^3 mod 33 = 2744 mod 33 = 5",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Decrypt: 5^7 mod 33 = 78125 mod 33 = 14",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene8_summary(self):
        self.add_subcaption(
            "Today we proved Euler's theorem using group theory, derived "
            "the exponent reduction corollary, and then built the entire "
            "RSA cryptosystem on top of it. The key insight is that "
            "Euler's theorem guarantees decryption recovers the original "
            "message. Next time we will explore primitive roots.",
            duration=28,
        )
        self.ly.section_divider(7, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("1. Euler's theorem: a^phi(n) = 1 (mod n)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Exponents reduce mod phi(n)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. RSA: ed = 1 (mod phi(n)) makes it work",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Security = hardness of factoring n = p*q",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()
        play_outro(self, "Euler's Theorem and RSA", "Number Theory")
