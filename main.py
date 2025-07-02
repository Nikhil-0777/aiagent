import streamlit as st
from dotenv import load_dotenv
from src.workflow import Workflow

load_dotenv()

# Initialize the workflow
workflow = Workflow()

st.set_page_config(page_title="Developer Tools Research Agent", page_icon="🔍")
st.title("🔍 Developer Tools Research Agent")

query = st.text_input("Enter a developer tool, API, framework, or platform to research:")

if query:
    with st.spinner("Searching and analyzing..."):
        result = workflow.run(query)

    st.markdown(f"### 📊 Results for: `{query}`")
    for i, company in enumerate(result.companies, 1):
        with st.expander(f"{i}. 🏢 {company.name}"):
            st.write(f"**🌐 Website**: {company.website}")
            st.write(f"**💰 Pricing**: {company.pricing_model}")
            st.write(f"**📖 Open Source**: {company.is_open_source}")

            if company.tech_stack:
                st.write(f"**🛠️ Tech Stack**: {', '.join(company.tech_stack[:5])}")
            if company.language_support:
                st.write(f"**💻 Language Support**: {', '.join(company.language_support[:5])}")
            if company.api_available is not None:
                api_status = "✅ Available" if company.api_available else "❌ Not Available"
                st.write(f"**🔌 API**: {api_status}")
            if company.integration_capabilities:
                st.write(f"**🔗 Integrations**: {', '.join(company.integration_capabilities[:4])}")
            if company.description and company.description != "Analysis failed":
                st.write(f"**📝 Description**: {company.description}")

    if result.analysis:
        st.markdown("### 🔧 Developer Recommendations")
        st.info(result.analysis)

st.markdown("---")
st.caption("Type a query and press enter to begin your research.")
