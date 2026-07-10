"""
Teka Permainan - satu permainan teka-teki Python untuk cabaran Coding for All.

Penulis: Putera Muhammad Luqmanul Hakim
Sekolah: Sekolah Kebangsaan Seksyen 10 Kota Damansara

Penafian: Program ini dihasilkan untuk tujuan pendidikan dan pertandingan
sebagai sebahagian daripada Cabaran Pengekodan Python "Coding for All"
anjuran Penang Science Cluster. Semua nama permainan yang disebut dalam
program ini adalah tanda dagangan dan hak milik pemilik masing-masing, dan
hanya digunakan sebagai kandungan permainan teka-teki; tiada hak milik atau
pertalian dituntut.
"""

import random

GAMES = {
    "Minecraft": [
        "Anda boleh melombong sumber dan membuat alatan.",
        "Terdapat Creeper yang meletup berhampiran anda.",
        "Dunia permainan ini dibina sepenuhnya daripada blok yang boleh diletak dan dimusnahkan.",
        "Steve dan Alex adalah kulit pemain lalai dalam permainan sandbox ini.",
        "Permainan ini dicipta oleh Markus 'Notch' Persson dan dilancarkan pada 2011.",
    ],
    "Among Us": [
        "Anda melaksanakan tugasan di atas sebuah kapal angkasa.",
        "Seorang atau lebih pemain secara rahsia cuba menggagalkan krew.",
        "Pemain boleh memanggil mesyuarat kecemasan untuk mengundi keluar seseorang.",
        "Angkasawan berbentuk kacang cuba mengesan 'impostor' sebelum semua orang dibunuh.",
        "Permainan ini meletup populariti pada 2020 hasil sokongan penstrim langsung.",
    ],
    "Fortnite": [
        "100 pemain berterjun payung ke sebuah pulau.",
        "Anda boleh membina dinding dan tanjakan daripada bahan yang dikumpul.",
        "Kawasan permainan mengecil apabila ribut semakin menghampiri.",
        "Pemain atau pasukan terakhir yang bertahan memenangi battle royale ini.",
        "Gerakan tarian seperti 'Floss' menjadi trend budaya popular dunia sebenar.",
    ],
    "Roblox": [
        "Sebenarnya ia sebuah platform penuh dengan permainan ciptaan pemain lain.",
        "Anda boleh mencipta pengalaman sendiri menggunakan bahasa skrip bernama Lua.",
        "Watak anda dibina daripada avatar berbentuk blok yang boleh disesuaikan.",
        "Mata wang dalam permainan ini dipanggil Robux.",
        "Platform ini dilancarkan pada 2006 dan membolehkan sesiapa sahaja mencipta permainan sendiri.",
    ],
    "Tetris": [
        "Bentuk yang jatuh perlu disusun tanpa meninggalkan ruang kosong.",
        "Membersihkan satu baris penuh akan menghilangkannya.",
        "Setiap kepingan terdiri daripada empat petak, dipanggil tetromino.",
        "Permainan teka-teki klasik ini dicipta di Kesatuan Soviet pada 1984.",
        "Penciptanya, Alexey Pajitnov, menamakannya sempena tenis dan perkataan Yunani untuk empat.",
    ],
    "Pac-Man": [
        "Anda bergerak melalui labirin sambil makan bintik-bintik kecil.",
        "Empat hantu sedang mengejar anda.",
        "Memakan bintik besar yang berkelip membolehkan anda memakan hantu buat seketika.",
        "Watak utama ialah bulatan kuning yang terkenal dengan bunyi mengunyahnya.",
        "Permainan arked klasik 1980 ini pada asalnya dipanggil 'Puck-Man' di Jepun.",
    ],
    "Chess": [
        "Dua pemain bergilir-gilir menggerakkan bidak di atas papan 8x8.",
        "Bidak paling berkuasa ialah ratu (queen).",
        "Matlamatnya ialah untuk mengadu raja lawan (checkmate).",
        "Permainan strategi purba ini menggunakan bidak seperti pion, kuda, dan gajah.",
        "Kejohanan dunia telah diadakan untuk permainan ini sejak tahun 1800-an.",
    ],
    "Flappy Bird": [
        "Anda menekan skrin untuk memastikan seekor burung terus terbang.",
        "Anda perlu mengelak paip hijau.",
        "Satu sentuhan pada halangan menamatkan permainan serta-merta.",
        "Permainan mudah alih yang terkenal sukar ini ditarik balik oleh penciptanya pada 2014.",
        "Penciptanya, Dong Nguyen, berkata permainan ini 'terlalu ketagihan' lalu menariknya.",
    ],
    "Grand Theft Auto V": [
        "Anda boleh mencuri kereta dan mengelak polis dalam dunia terbuka.",
        "Permainan ini berlatarkan negeri fiksyen San Andreas.",
        "Anda mengawal tiga watak berbeza sepanjang cerita.",
        "Rompakan dalam talian berbilang pemain membolehkan anda merompak bank bersama rakan.",
        "Dibangunkan oleh Rockstar Games, ia antara produk hiburan paling laris pernah dijual.",
    ],
    "Call of Duty": [
        "Anda bertempur dalam tembak-menembak orang pertama yang pantas.",
        "Mod berbilang pemain popular termasuk Team Deathmatch dan Search and Destroy.",
        "Spin-off battle royale-nya dipanggil Warzone.",
        "Misi kempen selalunya berdasarkan konflik ketenteraan moden atau sejarah.",
        "Diterbitkan oleh Activision, siri ini mengeluarkan tajuk baharu hampir setiap tahun.",
    ],
    "League of Legends": [
        "Dua pasukan lima orang bertarung untuk memusnahkan pangkalan musuh.",
        "Pemain memilih seorang wira unik dipanggil 'champion' sebelum setiap perlawanan.",
        "Menara, minion, dan raksasa hutan memenuhi medan perang.",
        "Ia antara permainan esports yang paling banyak ditonton di dunia.",
        "MOBA ini dibangunkan oleh Riot Games dan sering disingkat 'LoL'.",
    ],
    "Brawl Stars": [
        "Anda mengawal watak dengan serangan unik dan kebolehan istimewa dalam perlawanan pantas 3 minit.",
        "Mod permainan termasuk Gem Grab, Brawl Ball, dan Knockout.",
        "Mengumpul permata dan memegangnya sehingga masa detik tamat memenangi satu mod popular.",
        "Permainan ini dibangunkan oleh studio Finland yang sama di sebalik permainan strategi membina kampung.",
        "Maskot berambut perang berdurinya, Shelly, muncul dalam kebanyakan bahan promosinya.",
    ],
    "Genshin Impact": [
        "Anda meneroka dunia terbuka sebagai seorang Pengembara mencari adik-beradik yang hilang.",
        "Watak boleh disummon melalui sistem gacha menggunakan mata wang dalam permainan.",
        "Kuasa unsur seperti Api, Air, dan Elektro bergabung untuk reaksi istimewa.",
        "Meluncur merentasi peta menggunakan glider ajaib adalah mekanik pergerakan utama.",
        "RPG aksi percuma ini dibangunkan oleh HoYoverse, berlatarkan dunia Teyvat.",
    ],
    "Super Mario Bros": [
        "Seorang tukang paip berkumis berlari dan melompat merentasi tahap platform berwarna-warni.",
        "Memijak musuh seperti Goomba akan mengalahkan mereka.",
        "Mengambil cendawan membesarkan watak anda.",
        "Matlamat setiap tahap selalunya untuk sampai ke tiang bendera.",
        "Puteri watak ini, Peach, kerap diculik oleh penjahat bernama Bowser.",
    ],
    "The Legend of Zelda": [
        "Anda meneroka kerajaan fantasi sambil menyelesaikan teka-teki dan gowa.",
        "Seorang wira ajaib tanpa usia bernama Link biasanya watak yang dimainkan.",
        "Triforce adalah artifak suci yang penting dalam cerita.",
        "Puteri Zelda sering perlu diselamatkan daripada penjahat Ganon.",
        "Siri lama Nintendo ini mengilhamkan banyak permainan aksi-pengembaraan lain.",
    ],
    "Mario Kart": [
        "Anda berlumba go-kart merentasi litar berwarna-warni penuh halangan.",
        "Kotak item memberi anda perkara seperti tempurung dan pisang untuk digunakan terhadap pesaing.",
        "Tempurung biru mengejar sesiapa yang berada di kedudukan pertama.",
        "Watak yang dikenali seperti Mario, Luigi, dan Bowser boleh dipilih sebagai peserta lumba.",
        "Spin-off perlumbaan Nintendo ini menjadi kegemaran malam permainan bersama rakan-rakan.",
    ],
    "Candy Crush Saga": [
        "Anda menukar kepingan berwarna-warni untuk membuat padanan tiga atau lebih.",
        "Gabungan istimewa dicipta dengan memadankan empat atau lima kepingan dalam satu baris.",
        "Setiap tahap mempunyai bilangan langkah atau masa terhad untuk mencapai matlamat.",
        "Gula-gula berjalur dan gula-gula berbalut membantu membersihkan papan.",
        "Permainan teka-teki mudah alih padan-tiga ini dibangunkan oleh King dan mempunyai beribu-ribu tahap.",
    ],
    "Subway Surfers": [
        "Anda berlari menuruni landasan kereta api, mengelak kereta api yang datang.",
        "Seorang pemeriksa yang garang bersama anjingnya mengejar anda sepanjang masa.",
        "Leret skrin membolehkan anda melompat, berguling, dan menukar lorong untuk mengelak halangan.",
        "Mengumpul syiling membolehkan anda membuka kunci watak dan papan apungan baharu.",
        "Endless runner ini memaparkan remaja yang suka mencorat-coret melarikan diri daripada undang-undang.",
    ],
    "Clash of Clans": [
        "Anda membina dan mempertahankan sebuah kampung menggunakan emas, elixir, dan dark elixir.",
        "Melatih bala tentera seperti Barbarian dan Archer membolehkan anda menyerang pangkalan pemain lain.",
        "Menyertai sebuah Clan membolehkan anda menderma tentera dan bertempur dalam Clan Wars.",
        "Menaik taraf Town Hall anda membuka bangunan dan pertahanan baharu.",
        "Permainan strategi mudah alih ini dibangunkan oleh Supercell dan menjadi fenomena global.",
    ],
    "Mobile Legends": [
        "Dua pasukan lima orang bertarung merentasi tiga lorong untuk memusnahkan pangkalan musuh.",
        "Pemain memilih seorang Hero unik dengan peranan istimewa seperti Tank, Marksman, atau Assassin.",
        "Mengetuk minion dan lorong membantu anda mengumpul emas dan pengalaman.",
        "Memusnahkan menara membuka laluan menuju teras musuh.",
        "MOBA mudah alih ini amat popular di Asia Tenggara dan dibuat oleh Moonton.",
    ],
}

MAX_GUESSES = len(next(iter(GAMES.values())))  # satu percubaan bagi setiap petunjuk yang ada
QUESTIONS_PER_ROUND = 5


# Pilih secara rawak QUESTIONS_PER_ROUND permainan berbeza daripada GAMES untuk satu pusingan.
def choose_round_games():
    try:
        return random.sample(list(GAMES.keys()), QUESTIONS_PER_ROUND)
    except ValueError as error:
        raise ValueError(
            f"Permainan tidak mencukupi dalam GAMES ({len(GAMES)}) untuk melengkapkan satu "
            f"pusingan {QUESTIONS_PER_ROUND} soalan."
        ) from error


# Dedahkan petunjuk satu demi satu untuk secret_game dan pulangkan markah peratusan yang diperoleh.
def play_question(secret_game):
    clues = GAMES[secret_game]
    attempts_used = 0

    print("\nSaya sedang memikirkan satu permainan. Cuba teka daripada petunjuk berikut!")

    while attempts_used < MAX_GUESSES:
        print(f"\nPetunjuk {attempts_used + 1}: {clues[attempts_used]}")
        guess = input("Teka anda: ").strip()
        attempts_used += 1

        if guess.lower() == secret_game.lower():
            mark = round((MAX_GUESSES - attempts_used + 1) / MAX_GUESSES * 100)
            print(f"\nBetul! Permainan itu ialah '{secret_game}'.")
            print(f"Anda meneka dengan betul dalam {attempts_used} percubaan. Markah: {mark}%")
            return mark

        remaining = MAX_GUESSES - attempts_used
        if remaining > 0:
            print(f"Belum tepat. {remaining} petunjuk lagi.")

    print(f"\nPercubaan telah habis! Permainan itu ialah '{secret_game}'.")
    return 0


# Jalankan satu pusingan QUESTIONS_PER_ROUND soalan dan cetak markah keseluruhan.
def play_round():
    round_games = choose_round_games()
    total_mark = 0

    print(f"\n=== Pusingan Baharu: {QUESTIONS_PER_ROUND} permainan untuk diteka! ===")

    for question_number, secret_game in enumerate(round_games, start=1):
        print(f"\n--- Soalan {question_number} daripada {QUESTIONS_PER_ROUND} ---")
        total_mark += play_question(secret_game)

    average_mark = round(total_mark / QUESTIONS_PER_ROUND)
    print(f"\n=== Pusingan selesai! Markah keseluruhan anda: {average_mark}% ===")


# Titik permulaan: alu-alukan pemain dan teruskan pusingan sehingga mereka berhenti.
def main():
    print("=== Teka Permainan ===")
    try:
        while True:
            play_round()
            again = input("\nMain pusingan lagi? (y/t): ").strip().lower()
            if again != "y":
                print("Terima kasih kerana bermain!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nPermainan terganggu. Terima kasih kerana bermain!")
    except ValueError as error:
        print(f"\nRalat persediaan: {error}")


if __name__ == "__main__":
    main()
