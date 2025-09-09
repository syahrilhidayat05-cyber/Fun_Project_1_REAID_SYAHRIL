import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Career Quiz", layout="centered")

st.title("🎯 Career Quiz - Temukan Profesi Cocokmu")
st.write("Jawab semua pertanyaan di bawah, lalu lihat hasil probabilitas profesi yang cocok!")

# --- Pertanyaan ---
questions = {
    "Apa aktivitas favoritmu?": [
        ("Menulis kode program", "Programmer"),
        ("Menganalisis data", "Data Scientist"),
        ("Menggambar & desain", "Designer"),
    ],
    "Apa gaya kerja yang kamu suka?": [
        ("Struktur & problem solving", "Programmer"),
        ("Logis & analitis", "Data Scientist"),
        ("Kreatif & imajinatif", "Designer"),
    ],
    "Mana yang lebih menarik buatmu?": [
        ("Membangun aplikasi/software", "Programmer"),
        ("Statistik & machine learning", "Data Scientist"),
        ("Seni & visual", "Designer"),
    ]
}

# --- Jawaban user ---
answers = {}
for q, opts in questions.items():
    answers[q] = st.radio(q, [o[0] for o in opts], index=None, key=q)

# --- Tombol hasil ---
if st.button("🔍 Lihat Hasil"):
    # cek apakah semua pertanyaan sudah dijawab
    if None in answers.values():
        st.warning("⚠️ Kamu harus menjawab semua pertanyaan dulu sebelum melihat hasil!")
    else:
        # Hitung skor
        scores = {"Programmer": 0, "Data Scientist": 0, "Designer": 0}
        for q, ans in answers.items():
            for text, job in questions[q]:
                if ans == text:
                    scores[job] += 1

        total = sum(scores.values())
        probabilities = {job: round((val / total) * 100, 1) for job, val in scores.items()}

        st.subheader("📊 Hasil Probabilitas Profesi:")
        for job, prob in probabilities.items():
            st.write(f"**{job}**: {prob}%")
            st.progress(int(prob))

        # --- Pie chart ---
        fig, ax = plt.subplots()
        ax.pie(probabilities.values(), labels=probabilities.keys(), autopct='%1.1f%%', startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

        # --- Cari hasil tertinggi ---
        max_val = max(probabilities.values())
        best_matches = [job for job, val in probabilities.items() if val == max_val]

        if len(best_matches) == 1:
            best = best_matches[0]
            st.success(f"Profesi yang paling cocok denganmu adalah: **{best}**")

            if best == "Programmer":
                st.image("https://img.icons8.com/external-flaticons-lineal-color-flat-icons/512/external-programmer-web-developer-flaticons-lineal-color-flat-icons.png", width=200)
            elif best == "Data Scientist":
                st.image("https://img.icons8.com/external-flaticons-lineal-color-flat-icons/512/external-data-scientist-data-analytics-flaticons-lineal-color-flat-icons.png", width=200)
            elif best == "Designer":
                st.image("https://img.icons8.com/external-flaticons-lineal-color-flat-icons/512/external-graphic-designer-design-thinking-flaticons-lineal-color-flat-icons.png", width=200)

        else:
            st.info("✨ Wah, hasilnya imbang! Kamu cocok di beberapa profesi berikut:")
            for job in best_matches:
                st.write(f"- {job}")