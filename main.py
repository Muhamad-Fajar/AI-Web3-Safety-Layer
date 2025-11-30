import random
import time
from datetime import datetime

class Web3SafetyLayer:
    def __init__(self, owner_address):
        self.owner_address = owner_address
        # Whitelist alamat yang aman (Simulasi)
        self.whitelisted_addresses = [
            "0x1234567890abcdef1234567890abcdef12345678", 
            "0xabcdef1234567890abcdef1234567890abcdef12"
        ]
        self.max_transaction_limit = 1.0 # ETH

    def validate_transaction(self, target_address, amount):
        """
        Fungsi Deterministik untuk memfilter keputusan AI.
        Ini adalah 'Rem' yang mencegah halusinasi.
        """
        print(f"\n[SAFETY LAYER] Memeriksa transaksi ke {target_address}...")
        time.sleep(1) # Simulasi proses checking

        # Cek 1: Validasi Format Address (Panjang harus 42 karakter & diawali 0x)
        if not target_address.startswith("0x") or len(target_address) != 42:
            return False, "ERROR: Format alamat tidak valid (Potensi Halusinasi AI)."

        # Cek 2: Apakah alamat ada di whitelist?
        if target_address not in self.whitelisted_addresses:
            return False, "RISK ALERT: Alamat tidak dikenal/tidak ada di whitelist."

        # Cek 3: Batas Limit Transaksi
        if amount > self.max_transaction_limit:
            return False, f"RISK ALERT: Jumlah {amount} ETH melebihi batas aman ({self.max_transaction_limit} ETH)."

        return True, "AMAN: Transaksi terverifikasi."

# --- SIMULASI AI (Mock AI) ---
def mock_ai_agent():
    """
    Simulasi AI yang kadang pintar, kadang 'halusinasi' (Probabilistik).
    """
    scenarios = [
        {"addr": "0x1234567890abcdef1234567890abcdef12345678", "amount": 0.5}, # Aman
        {"addr": "0xScammerAddress123", "amount": 0.5},                       # Format Salah
        {"addr": "0x9999999999abcdef1234567890abcdef12345678", "amount": 0.2}, # Tidak Whitelist
        {"addr": "0xabcdef1234567890abcdef1234567890abcdef12", "amount": 5.0}  # Limit Jebol
    ]
    return random.choice(scenarios)

# --- EKSEKUSI UTAMA ---
if __name__ == "__main__":
    print("=== MEMULAI AUTONOMOUS AGENT DENGAN SAFETY LAYER ===\n")
    
    # Setup Wallet Pemilik
    my_layer = Web3SafetyLayer(owner_address="0xMe")

    # Simulasi 3 Transaksi
    for i in range(1, 4):
        print(f"--- Percobaan Transaksi #{i} ---")
        
        # 1. AI Berpikir (Probabilistik)
        print("🤖 AI sedang menganalisa pasar...")
        time.sleep(1)
        decision = mock_ai_agent()
        print(f"🤖 AI Menyarankan: Kirim {decision['amount']} ETH ke {decision['addr']}")

        # 2. Safety Layer Bekerja (Deterministik)
        is_safe, message = my_layer.validate_transaction(decision['addr'], decision['amount'])

        # 3. Keputusan Akhir
        if is_safe:
            print(f"✅ EKSEKUSI BERHASIL: {message}")
            # Di sini kode web3.py asli akan dijalankan
        else:
            print(f"⛔ TRANSAKSI DIBLOKIR: {message}")
        
        print("-" * 30)
