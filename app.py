import streamlit as st

st.title("🏥 AI Health Recommendation System")

st.write("Enter your details below:")

# User inputs
age = st.number_input("Enter your age", 1, 100)

symptoms = st.text_area("Enter your symptoms (e.g., fever, cough, headache)")

sleep = st.slider("Hours of sleep per day", 0, 12, 6)

exercise = st.slider("Exercise days per week", 0, 7, 2)

diet = st.selectbox("Diet type", ["Healthy", "Average", "Unhealthy"])

# Button
if st.button("Get Recommendation"):

    st.subheader("📊 Health Analysis")

    # Symptom checking
    if "fever" in symptoms.lower():
        st.warning("Possible viral infection symptoms detected.")

    if "cough" in symptoms.lower():
        st.warning("Respiratory symptoms detected.")

    # Sleep check
    if sleep < 5:
        st.error("Low sleep detected. It may affect immunity.")

    elif sleep < 7:
        st.info("Try to improve sleep to at least 7 hours.")

    else:
        st.success("Good sleep habits!")

    # Exercise check
    if exercise < 2:
        st.warning("Low physical activity. Try to exercise more.")

    else:
        st.success("Good activity level!")

    # Diet check
    st.subheader("🥗 Recommendations")

    if diet == "Unhealthy":
        st.write("• Eat more fruits and vegetables")
        st.write("• Avoid junk food")
    elif diet == "Average":
        st.write("• Improve diet quality slightly")
    else:
        st.write("• Maintain your healthy diet")

    # General advice
    st.write("• Drink 2–3 liters of water daily")
    st.write("• Maintain good hygiene")
    st.write("• Consult doctor if symptoms persist")