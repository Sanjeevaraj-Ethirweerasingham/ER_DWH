import streamlit as st
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="ER Management Dashboard", 
    layout="wide",
    initial_sidebar_state="collapsed")

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 10px;
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        font-size: 1.1rem;
        opacity: 0.9;
        margin: 0;
    }
    
    .nav-button {
        background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%);
        border: none;
        color: white;
        padding: 1rem 1.5rem;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 1rem;
        margin: 0.2rem;
        cursor: pointer;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        width: 100%;
        height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .nav-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    .central-button {
        background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%);
        border: none;
        color: white;
        padding: 1.5rem 2rem;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        border-radius: 15px;
        box-shadow: 0 6px 25px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        width: 100%;
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .central-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    }
    
    .query-container {
        background: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 2rem 0;
        border-left: 5px solid #667eea;
    }
    
    .query-header {
        color: #333;
        font-size: 1.8rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .back-button {
        background: linear-gradient(45deg, #ff6b6b, #ee5a24);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-top: 1rem;
    }
    
    .back-button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(255,107,107,0.3);
    }
    
    .process-flow {
        background: #f8f9ff;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        font-weight: 600;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🏥 EMERGENCY ROOM DATA WAREHOUSE</h1>
    <p>Queries & Architecture Plans</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = 'menu'

# Navigation Menu
if st.session_state['page'] == 'menu':
        
    # Query Navigation Buttons
    st.markdown("### One to One Relationship Queries - Visitwise")
    st.markdown("### 🔍 ER Admission to Discharge Queries")
    
    # First Row: 5 boxes
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("🏥\n\nAdmissions", key="admission"):
            st.session_state['page'] = 'admission'
            st.rerun()
    
    with col2:
        if st.button("👁️\n\nVisual Triage", key="visual_triage"):
            st.session_state['page'] = 'visual_triage'
            st.rerun()
    
    with col3:
        if st.button("🩺\n\nMain Triage", key="main_triage"):
            st.session_state['page'] = 'main_triage'
            st.rerun()
    
    with col4:
        if st.button("👨‍⚕️\n\nStaff\nAssignments", key="assignments"):
            st.session_state['page'] = 'assignments'
            st.rerun()
    
    with col5:
        if st.button("🚪\n\nDischarge", key="discharge"):
            st.session_state['page'] = 'discharge'
            st.rerun()

    # Second Row: ER Journey
    st.markdown("### 🛤️ Patient Journey")
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("🛤️ ER Patient Journey", key="er_journey"):
            st.session_state['page'] = 'er_journey'
            st.rerun()

    
    # Central Button
    st.markdown("### 📊 ER Patient Details (One to One Flat table)")
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("📋 **ER Patient Flaat table **", key="er_patient_data"):
            st.session_state['page'] = 'er_patient_data'
            st.rerun()


    # Process Flow Diagram
    st.markdown("""
    <div class="process-flow">
        <h3 style="text-align: center; color: #333; margin-bottom: 2rem;">🔄 ER Patient Flow</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Create process flow using Plotly
    fig = go.Figure()
    
    # Define positions for nodes
    nodes = {
        'Admission': (1, 2),
        'Visual Triage': (2, 2),
        'Main Triage': (3, 2),
        'Assignments': (4, 2),
        'Discharge': (5, 2),
        'ER Patient\nDetails': (3, 1)
    }
    
    colors = {
        'Admission': '#ff6b6b',
        'Visual Triage': '#4ecdc4',
        'Main Triage': '#45b7d1',
        'Assignments': '#96ceb4',
        'Discharge': '#feca57',
        'ER Patient\nDetails': '#667eea'
    }
    
    # Add nodes
    for node, (x, y) in nodes.items():
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(size=60, color=colors[node], opacity=0.8),
            text=node,
            textposition='middle center',
            textfont=dict(color='white', size=10, family='Arial Black'),
            showlegend=False,
            hovertemplate=f'<b>{node}</b><extra></extra>'
        ))

    
    # Add arrows to central hub
    for node, (x, y) in nodes.items():
        if node != 'ER Patient\nData Hub':
            fig.add_trace(go.Scatter(
                x=[x, 3], y=[y, 1],
                mode='lines',
                line=dict(color='rgba(102, 126, 234, 0.6)', width=3),
                showlegend=False,
                hoverinfo='skip'
            ))
    
    fig.update_layout(
        title=dict(
            text="Emergency Room Patient Flow Architecture",
            x=0.5,
            font=dict(size=18, color='#333')
        ),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 6]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.5, 2.5]),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)



    # Third Row: ER Diagnosis
    st.markdown("### 🛤️ Patient Diagnosis")
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("🛤️ ER Patient Diagnosis \n\n\nOne to Many Relationship", key="er_diagnosis"):
            st.session_state['page'] = 'er_diagnosis'
            st.rerun()
    
    # Fourth Row: ER Diagnosis
    st.markdown("### 🛤️ Patient Medications")
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("🛤️ ER Patient Medications \n\n\nOne to Many Relationship", key="er_medications"):
            st.session_state['page'] = 'er_medications'
            st.rerun()

    # Fifth Row: ER Procedures
    st.markdown("### 🛤️ Patient Procedures")
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("🛤️ ER Patient Procedures \n\n\nOne to Many Relationship", key="er_procedures"):
            st.session_state['page'] = 'er_procedures'
            st.rerun()

    # Sixth Row: ER Lab Details
    st.markdown("### 🛤️ ER Patient Lab Details")
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("🛤️ ER Patient Lab Details \n\n\nOne to Many Relationship", key="er_lab_details"):
            st.session_state['page'] = 'er_lab_details'
            st.rerun()

    # Seventh Row: ER Patient Master Data
    st.markdown("### 🛤️ ER Patient Master Data")
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("🛤️ ER Patient Master Data \n\n\nSlowly Changing Dimensions", key="er_patient_master"):
            st.session_state['page'] = 'er_patient_master'
            st.rerun()

    # Eighth Row: ER Employee Master Data
    st.markdown("### 🛤️ ER Employee Master Data")
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("🛤️ ER Employee Master Data \n\n\nSlowly Changing Dimensions", key="er_employee_master"):
            st.session_state['page'] = 'er_employee_master'
            st.rerun()

# Query Pages
def render_query_page(title, icon, query, description=""):
    st.markdown(f"""
    <div class="query-container">
        <h2 class="query-header">{icon} {title}</h2>
        {f'<p style="color: #666; font-size: 1.1rem; margin-bottom: 1.5rem;">{description}</p>' if description else ''}
    </div>
    """, unsafe_allow_html=True)
    
    # Query display with syntax highlighting
    st.code(query, language="sql")
    
    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        if st.button("⬅️ Back to Menu", key="back"):
            st.session_state['page'] = 'menu'
            st.rerun()
    with col2:
        st.button("📋 Copy Query", key="copy")
    
    # Add query execution info
    st.info("💡 **Tip:** Replace `${max_updated_time}` with your desired timestamp in 'YYYY-MM-DD HH24:MI:SS.FF7' format")

# Page routing
if st.session_state['page'] == 'admission':
    render_query_page(
        "Admission Management",
        "🏥",
        """SELECT 
    ep.HOSPITALID AS hospital_id,
    ep.patientpomrid AS visit_id,
    aa.ADMISSION_ID AS er_admission_id,
    ep.patientid AS patient_id,
    ep.arrivedtime AS arrived_time,
    ep.eraction AS latest_action_status,
    ep.erpatientstatus AS latest_admission_status,
    ep.isnursingservices AS is_nursing_services,
    ep.hospitalgroupid AS tenant_id,
    ep.clinicgroupid AS clinic_group_id,
    ep.clinicid AS clinic_id,
    ep.isactive AS is_active,
    ep.modifiedon
FROM er_erfun.erfun_patientgriddata ep
JOIN AD_REQUEST.ADMLM_ADMISSION aa ON aa.PATIENT_POMR_ID = ep.PATIENTPOMRID AND aa.IS_FROM_ER = 1
WHERE ep.modifiedon > TO_TIMESTAMP('${max_updated_time}', 'YYYY-MM-DD HH24:MI:SS.FF7')
ORDER BY ep.modifiedon DESC""",
        "Retrieve patient admission data with hospital and clinic information"
    )

elif st.session_state['page'] == 'visual_triage':
    render_query_page(
        "Visual Triage Assessment",
        "👁️",
        """WITH first_record AS (
    SELECT *
    FROM (
        SELECT 
            epv.patientpomrid,
            TO_NUMBER(JSON_VALUE(epv.scoreobject, '$.COVID19')) AS first_covid_score,
            TO_NUMBER(JSON_VALUE(epv.scoreobject, '$.MERS'))    AS first_mers_score,
            epv.createdon AS first_createdon,
            epv.createdby AS first_createdby,
            epv.modifiedon AS first_modifiedon,
            ROW_NUMBER() OVER (PARTITION BY epv.patientpomrid ORDER BY epv.createdon ASC) AS rn
        FROM er_erfun.erfun_patientvisualtriagescore epv
        WHERE epv.templatecode = 'ER_MOH_VISUAL_TRIAGE_TEMPLATE'
    ) t
    WHERE rn = 1
),
last_record AS (
    SELECT *
    FROM (
        SELECT 
            epv.patientpomrid,
            TO_NUMBER(JSON_VALUE(epv.scoreobject, '$.COVID19')) AS last_covid_score,
            TO_NUMBER(JSON_VALUE(epv.scoreobject, '$.MERS'))    AS last_mers_score,
            epv.createdon AS last_createdon,
            epv.createdby AS last_createdby,
            epv.modifiedon AS last_modifiedon,
            ROW_NUMBER() OVER (PARTITION BY epv.patientpomrid ORDER BY epv.createdon DESC) AS rn
        FROM er_erfun.erfun_patientvisualtriagescore epv
        WHERE epv.templatecode = 'ER_MOH_VISUAL_TRIAGE_TEMPLATE'
    ) t
    WHERE rn = 1
),
joined_records AS (
    SELECT 
        f.patientpomrid AS visit_id,
        f.first_covid_score,
        f.first_mers_score,
        f.first_createdon,
        f.first_createdby,
        f.first_modifiedon,
        l.last_covid_score,
        l.last_mers_score,
        l.last_createdon,
        l.last_createdby,
        l.last_modifiedon
    FROM first_record f
    JOIN last_record l ON f.patientpomrid = l.patientpomrid
)
SELECT 
    jr.*
FROM joined_records jr
WHERE jr.last_modifiedon > TO_TIMESTAMP('${max_updated_time}', 'YYYY-MM-DD HH24:MI:SS.FF7')""",
        "Track COVID-19 and MERS visual triage scores from first to latest assessment"
    )

elif st.session_state['page'] == 'main_triage':
    render_query_page(
        "Main Triage Evaluation",
        "🩺",
        """WITH first_record AS (
    SELECT *
    FROM (
        SELECT 
            ep.patientpomrid,
            ep.eraction,
            ep.createdon,
            ep.createdby,
            ROW_NUMBER() OVER (PARTITION BY ep.patientpomrid ORDER BY ep.createdon ASC) AS rn,
            ep.MODIFIEDON, 
            ep.ERACTIONRESULT
        FROM er_erfun.erfun_patientjourney ep
        WHERE ep.eraction = 'TriageDone'
    ) t
    WHERE rn = 1
),
last_record AS (
    SELECT *
    FROM (
        SELECT 
            ep.patientpomrid,
            ep.eraction,
            ep.createdon,
            ep.createdby,
            ROW_NUMBER() OVER (PARTITION BY ep.patientpomrid ORDER BY ep.createdon DESC) AS rn,
            ep.MODIFIEDON, 
            ep.ERACTIONRESULT
        FROM er_erfun.erfun_patientjourney ep
        WHERE ep.eraction = 'TriageDone'
    ) t
    WHERE rn = 1
)
SELECT 
    f.patientpomrid as visit_id,
    f.eraction AS first_eraction,
    f.createdon AS first_createdon,
    f.createdby AS first_createdby,
    f.ERACTIONRESULT AS first_triagescore,
    l.eraction AS last_eraction,
    l.createdon AS last_createdon,
    l.createdby AS last_createdby,
    l.ERACTIONRESULT AS last_triagescore,
    l.modifiedon AS last_modifiedon
FROM first_record f
JOIN last_record l ON f.patientpomrid = l.patientpomrid
WHERE l.modifiedon > TO_TIMESTAMP('${max_updated_time}', 'YYYY-MM-DD HH24:MI:SS.FF7')""",
        "Monitor comprehensive triage evaluations and scoring progression"
    )

elif st.session_state['page'] == 'assignments':
    render_query_page(
        "Staff Assignment Management",
        "👨‍⚕️",
        """WITH first_doctor AS (
    SELECT *
    FROM (
        SELECT 
            ep.patientpomrid,
            ep.assignid AS first_assigned_doctor_id,
            ep.createdon AS first_doctor_assigned_on,
            ep.createdby AS first_doctor_assigned_by,
            ROW_NUMBER() OVER (PARTITION BY ep.patientpomrid ORDER BY ep.createdon ASC) AS rn
        FROM er_erfun.erfun_patientassignment ep
        WHERE ep.assigntype = 1
    ) t
    WHERE rn = 1
),
last_doctor AS (
    SELECT *
    FROM (
        SELECT 
            ep.patientpomrid,
            ep.assignid AS last_assigned_doctor_id,
            ep.createdon AS last_doctor_assigned_on,
            ep.createdby AS last_doctor_assigned_by,
            ep.modifiedon AS last_doctor_modified_on,
            ROW_NUMBER() OVER (PARTITION BY ep.patientpomrid ORDER BY ep.createdon DESC) AS rn
        FROM er_erfun.erfun_patientassignment ep
        WHERE ep.assigntype = 1
    ) t
    WHERE rn = 1
),
first_nurse AS (
    SELECT *
    FROM (
        SELECT 
            ep.patientpomrid,
            ep.assignid AS first_assigned_nurse_id,
            ep.createdon AS first_nurse_assigned_on,
            ep.createdby AS first_nurse_assigned_by,
            ROW_NUMBER() OVER (PARTITION BY ep.patientpomrid ORDER BY ep.createdon ASC) AS rn
        FROM er_erfun.erfun_patientassignment ep
        WHERE ep.assigntype = 2
    ) t
    WHERE rn = 1
),
last_nurse AS (
    SELECT *
    FROM (
        SELECT 
            ep.patientpomrid,
            ep.assignid AS last_assigned_nurse_id,
            ep.createdon AS last_nurse_assigned_on,
            ep.createdby AS last_nurse_assigned_by,
            ep.modifiedon AS last_nurse_modified_on,
            ROW_NUMBER() OVER (PARTITION BY ep.patientpomrid ORDER BY ep.createdon DESC) AS rn
        FROM er_erfun.erfun_patientassignment ep
        WHERE ep.assigntype = 2
    ) t
    WHERE rn = 1
)
SELECT
    fd.patientpomrid AS visit_id,
    fd.first_assigned_doctor_id,
    fd.first_doctor_assigned_on,
    fd.first_doctor_assigned_by,
    ld.last_assigned_doctor_id,
    ld.last_doctor_assigned_on,
    ld.last_doctor_assigned_by,
    fn.first_assigned_nurse_id,
    fn.first_nurse_assigned_on,
    fn.first_nurse_assigned_by,
    ln.last_assigned_nurse_id,
    ln.last_nurse_assigned_on,
    ln.last_assigned_nurse_assigned_by,
    ld.LAST_DOCTOR_MODIFIED_ON,
    ln.LAST_NURSE_MODIFIED_ON 
FROM first_doctor fd
LEFT JOIN last_doctor ld ON fd.patientpomrid = ld.patientpomrid
LEFT JOIN first_nurse fn ON fd.patientpomrid = fn.patientpomrid
LEFT JOIN last_nurse ln ON fd.patientpomrid = ln.patientpomrid
WHERE ( ld.LAST_DOCTOR_MODIFIED_ON > TO_TIMESTAMP('${doctor_update_time}', 'YYYY-MM-DD HH24:MI:SS.FF7')
      OR ln.LAST_NURSE_MODIFIED_ON > TO_TIMESTAMP('${nurse_update_time}', 'YYYY-MM-DD HH24:MI:SS.FF7') )""",
        "Track doctor and nurse assignments from initial to current assignments"
    )

elif st.session_state['page'] == 'discharge':
    render_query_page(
        "Discharge Processing",
        "🚪",
        """WITH discharge_details AS (
    SELECT 
        edp.patientpomrid AS visit_id,
        edp.eraction,
        edp.dischargedtime,
        edp.isdeceased,
        edp.istransferedtomorgue,
        edp.transferedtomorguedate,
        edp.MODIFIEDON 
    FROM er_erfun.erfun_dischargedetails ed
    INNER JOIN er_erfun.erfun_dischargedpatientgriddata edp
        ON edp.referenceid = ed.dischargedetailsrevisionid
       AND edp.eraction = 'Discharged'
    WHERE ed.isactive = 1
    AND edp.modifiedon > TO_TIMESTAMP('${max_update_time}', 'YYYY-MM-DD HH24:MI:SS.FF7')

    UNION ALL

    SELECT 
        edp.patientpomrid AS visit_id,
        edp.eraction,
        edp.dischargedtime,
        edp.isdeceased,
        edp.istransferedtomorgue,
        edp.transferedtomorguedate,
        edp.MODIFIEDON
    FROM er_erfun.erfun_dischargedpatientgriddata edp
    WHERE edp.referenceid = 0
      AND edp.eraction IN ('AdmittedToIp', 'LWBSDischarged')
      AND edp.arrivedtime IS NOT NULL
      AND edp.modifiedon > TO_TIMESTAMP('${max_update_time}', 'YYYY-MM-DD HH24:MI:SS.FF7')
)
SELECT *
FROM discharge_details""",
        "Monitor patient discharge processes including admissions and special cases"
    )

elif st.session_state['page'] == 'er_patient_data':
    st.markdown("""
    <div class="query-container">
        <h2 class="query-header">📋 Complete ER Patient Data View</h2>
        <p style="color: #666; font-size: 1.1rem; margin-bottom: 1.5rem;">
            Comprehensive view combining all patient data from admission to discharge
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""-- er_dwh.er_patient_data_view source
CREATE OR REPLACE VIEW er_dwh.er_patient_data_view
AS SELECT 
    ea.visit_id AS "Visit ID",
    rh.hospital_name AS "Hospital",
    rh.id AS hospital_id,
    ea.patient_id AS "Patient ID",
    concat(epd.firstname, ' ', epd.middlename, ' ', epd.thirdname, ' ', epd.lastname) AS "Patient Name",
    epd.idtype AS "Identification Type",
    epd.idnumber AS "Identification Number",
    ea.arrived_time AS "Admitted On",
    ea.latest_action_status AS "Latest Action Status",
    ea.is_nursing_services AS "IS Nursing Services",
    rc.clinic_description AS "Clinic Name",
    evt.first_covid_score AS "First Covid Score",
    evt.first_mers_score AS "First MERS Score",
    evt.first_createdon AS "First Visual Triage On",
    evt.last_covid_score AS "Last Covid Score",
    evt.last_mers_score AS "Last MERS Score",
    evt.last_createdon AS "Last Visual Triage On",
    emt.first_triagescore AS "First Triage Score",
    emt.first_createdon AS "First Triage On",
    emt.last_triagescore AS "Last Triage Score",
    emt.last_createdon AS "Last Triage On",
    ee.employee_name AS "First Assigned Doctor",
    eas.first_doctor_assigned_on AS "First Doctor Assigned On",
    ee1.employee_name AS "Last Assigned Doctor",
    eas.last_doctor_assigned_on AS "Last Doctor Assigned On",
    ee2.employee_name AS "First Assigned Nurse",
    eas.first_nurse_assigned_on AS "First Nurse Assigned On",
    ee3.employee_name AS "Last Assigned Nurse",
    eas.last_nurse_assigned_on AS "Last Nurse Assigned On",
    ed.eraction AS "Discharge Type",
    ed.dischargedtime AS "Discharge Time",
    ed.isdeceased AS "IS Deceased",
    ed.istransferedtomorgue AS "IS Transferred to Morgue"
FROM er_dwh.er_admissions ea
LEFT JOIN er_dwh.er_visual_triage evt ON evt.visit_id::numeric = ea.visit_id
LEFT JOIN er_dwh.er_main_triage emt ON emt.visit_id::numeric = ea.visit_id
LEFT JOIN er_dwh.er_assignments eas ON eas.visit_id::numeric = ea.visit_id
LEFT JOIN er_dwh.er_discharge ed ON ed.visit_id::numeric = ea.visit_id
LEFT JOIN rm_masterdata.rmmsd_hospital rh ON ea.hospital_id = rh.id::numeric
LEFT JOIN rm_masterdata.rmmsd_clinic rc ON rc.id = ea.clinic_id
LEFT JOIN er_dwh_sub_tables.er_patient_details epd ON epd.patientid::numeric = ea.patient_id
LEFT JOIN er_dwh_sub_tables.employees ee ON ee.employee_id = eas.first_assigned_doctor_id
LEFT JOIN er_dwh_sub_tables.employees ee1 ON ee1.employee_id = eas.last_assigned_doctor_id
LEFT JOIN er_dwh_sub_tables.employees ee2 ON ee2.employee_id = eas.first_assigned_nurse_id
LEFT JOIN er_dwh_sub_tables.employees ee3 ON ee3.employee_id = eas.last_assigned_nurse_id;""", language="sql")
    
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        if st.button("⬅️ Back to Menu", key="back_main"):
            st.session_state['page'] = 'menu'
            st.rerun()
    with col2:
        st.button("📋 Copy Query", key="copy_main")
    
    st.success("🎯 **This view provides a complete 360° view of each patient's ER journey**")

elif st.session_state['page'] == 'er_journey':
    render_query_page(
        "Patient Journey Timeline",
        "🛤️",
        """SELECT 
    pj.patientpomrid AS "Visit ID",
    rh.hospital_name AS "Hospital",
    pj.patientid AS "Patient ID",
    pj.modified_on as "Modified On",
    MIN(
        CASE
            WHEN pj.eraction::text = 'Arrived'::text THEN pj.createdon
            ELSE NULL::timestamp without time zone
        END) AS "Admitted On",
    MIN(
        CASE
            WHEN pj.eraction::text = ANY (ARRAY['DoctorAssigned'::character varying::text, 'InitialAssessmentStarted'::character varying::text]) THEN pj.createdon
            ELSE NULL::timestamp without time zone
        END) AS "Doctor Seen On",
    MAX(
        CASE
            WHEN pj.eraction::text = 'InitialAssessmentStarted'::text THEN pj.createdon
            ELSE NULL::timestamp without time zone
        END) AS "Initial Assessment On",
MIN(
    CASE
        WHEN pj.eraction::text IN (
            'DoctorDischarged',
            'AdmittedToIp',
            'Transfered',
            'DischargRequested',
            'AdmissionRequested',
            'ConsultationAdded',
            'DoctorTransferRequested',
            'PendingTransferToIPD'
        ) 
        THEN pj.createdon
        ELSE NULL::timestamp without time zone
    END
) AS "Decision On"
    MIN(
        CASE
            WHEN pj.eraction::text = ANY (ARRAY['Discharged'::character varying::text, 'AdmittedToIp'::character varying::text, 'Transfered'::character varying::text]) THEN pj.createdon
            ELSE NULL::timestamp without time zone
        END) AS "Disposition On",
    MAX(
        CASE
            WHEN pj.eraction::text = 'DoctorDischarged'::text THEN pj.createdon
            ELSE NULL::timestamp without time zone
        END) AS "Doctor Discharge Decision On",
    MAX(
        CASE
            WHEN pj.eraction::text = 'AdmissionRequested'::text THEN pj.createdon
            ELSE NULL::timestamp without time zone
        END) AS "IP Admission Decision On",
    MAX(
        CASE
            WHEN pj.eraction::text = 'AdmittedToIp'::text THEN pj.createdon
            ELSE NULL::timestamp without time zone
        END) AS "IP Admission Disposition On"
FROM er_dwh_sub_tables.patient_journey pj
JOIN rm_masterdata.rmmsd_hospital rh ON rh.id::numeric = pj.hospital_id
GROUP BY pj.patientpomrid, pj.patientid, rh.hospital_name;""",
        "Track complete patient journey timeline from admission through final disposition"
    )

elif st.session_state['page'] == 'er_diagnosis':
    render_query_page(
        "Patient Diagnosis",
        "🛤️",
        """SELECT 
epp.PATIENT_PROBLEM_REVISION_ID AS diagnosis_id,
epp.pomr_id as visit_id,  
epp.admission_id,
aa.ADMITTED_DATE, 
epp.PATIENT_ID,
epp.CREATED_ON as diagnosis_added_on, 
epp.condition,
epp.doctor_id,
epp.diagnosis_type, 
epp.selected_icd_code,
epp.selected_disease,
epp.MODIFIED_ON, 
epp.hospital_id
FROM eh_pomr.ehpom_patient_problem epp
join ad_request.admlm_admission aa on aa.admission_id = epp.admission_id and aa.is_from_er = 1
WHERE epp.MODIFIED_ON > TO_TIMESTAMP('2024-12-31 23:59:59', 'YYYY-MM-DD HH24:MI:SS')""")
    
elif st.session_state['page'] == 'er_medications':
    render_query_page(
        "Patient Medications",
        "🛤️",
        """SELECT
	prm.hospitalid,
    prm.regular_medication_details_id,
    prm.patient_pomr_id,
    epp.patient_id,
    prm.createdon AS prescribed_date,
    prm.formulary_name,
    pbt.brand_name,
    pmdd.createdon AS dispense_date,
    prm.modifiedon AS prescription_modifiedon,
    pmdd.modifiedon AS dispense_modifiedon
FROM ph_pharmacy.phbas_pres_reg_medicine prm 
JOIN eh_pomr.ehpom_patient_pomr epp
    ON epp.patient_pomr_id = prm.patient_pomr_id
LEFT JOIN (
    SELECT 
        createdon,
        med_detail_id,
        brand_id,
        medication_type_alias,
        modifiedon
    FROM ph_pharmacy.phbas_mar_dispense_details
) pmdd
    ON pmdd.med_detail_id = prm.regular_medication_details_id
   AND pmdd.medication_type_alias = 'REGULAR'
LEFT JOIN ph_pharmacy.phbas_brand_translate pbt
    ON pbt.brand_item_id = pmdd.brand_id
WHERE prm.clinicid = '350'
  AND (
        prm.modifiedon > TO_TIMESTAMP('${prescription_update_time}', 'YYYY-MM-DD HH24:MI:SS.FF7')
     OR pmdd.modifiedon > TO_TIMESTAMP('${dispense_update_time}', 'YYYY-MM-DD HH24:MI:SS.FF7')
  )	
  
  UNION ALL
  
  SELECT
    prm.IV_MEDICATION_DETAIL_ID,
	prm.hospitalid,
    prm.patient_pomr_id,
    epp.patient_id,
    prm.createdon AS prescribed_date,
    prm.formulary_name,
    pbt.brand_name,
    pmdd.createdon AS dispense_date,
    prm.modifiedon AS prescription_modifiedon,
    pmdd.modifiedon AS dispense_modifiedon
FROM PH_PHARMACY.PHBAS_PRES_IV_MEDICINE prm 
JOIN eh_pomr.ehpom_patient_pomr epp
    ON epp.patient_pomr_id = prm.patient_pomr_id
LEFT JOIN (
    SELECT 
        createdon,
        med_detail_id,
        brand_id,
        medication_type_alias,
        modifiedon
    FROM ph_pharmacy.phbas_mar_dispense_details
) pmdd
    ON pmdd.med_detail_id = prm.IV_MEDICATION_DETAIL_ID 
   AND pmdd.medication_type_alias = 'IV'
LEFT JOIN ph_pharmacy.phbas_brand_translate pbt
    ON pbt.brand_item_id = pmdd.brand_id
WHERE prm.clinic_name = 'EMERGENCY CLINIC' 
  AND (
        prm.modifiedon > TO_TIMESTAMP('${prescription_update_time}', 'YYYY-MM-DD HH24:MI:SS.FF7')
     OR pmdd.modifiedon > TO_TIMESTAMP('${dispense_update_time}', 'YYYY-MM-DD HH24:MI:SS.FF7')
  )
  """)
    
elif st.session_state['page'] == 'er_procedures':
    render_query_page(
        "Patient Procedures",
        "🛤️",
        """SELECT 
patient_order_id        as "patient_order_id",
pomr_id                 as "pomr_id",
patient_id              as "patient_id",
created_on              as "order_create_date",
procedure_code          as "procedure_code",
procedure_name          as "procedure_name",
sub_group_description   as "sub_group_description",
group_description       as "group_description",
category_description    as "category_description",
is_package              as "is_package",
is_surgery_procedure    as "is_surgery_procedure",
doctor_name             as "doctor_name",
invoice_status          as "invoice_status",
order_status            as "order_status",
cancel_reason           as "cancel_reason",
modified_on             as "modified_on",
hospital_id             as "hospital_id"
FROM eh_commmon.ehcom_patient_procedure_order epp
WHERE clinic_group_id = 400""")
    
elif st.session_state['page'] == 'er_lab_details':
    render_query_page(
        "ER Lab Details",
        "🛤️",
        """SELECT epp.patient_id AS "Patient ID",
    ea.arrived_time AS "Admitted On",
    epp.pomr_id AS "Visit ID",
    ll.patientorderid AS "Patient Order ID",
    epp.order_create_date AS "Patient Order Created Date",
    epp.doctor_name AS "Ordered Doctor",
    ll.createdon AS "Lab Order Created On",
    ee.employee_name AS "Lab Order Created By",
    lo.createdon AS "Sample Collected On",
    ee1.employee_name AS "Sample Collected By",
    COALESCE(lv.packagename, lt.packagename) AS "Package Name",
    COALESCE(lv.testdescription, lt.testdescription) AS "Test Name",
    COALESCE(lv.resultedon, lt.resultedon) AS "Resulted On",
    COALESCE(ee2.employee_name, ee3.employee_name) AS "Resulted By",
    COALESCE(lv.testresult, lt.finalresult) AS "Results",
    COALESCE(lv.primaryverifiedon, lt.primaryverifiedon) AS "Primary Verification On",
    COALESCE(ee4.employee_name, ee5.employee_name) AS "Primary Verification By",
    COALESCE(lv.medicalverifiedon, lt.medicalverifiedon) AS "Medical Verificarion On",
    COALESCE(ee6.employee_name, ee7.employee_name) AS "Medical Verification By"
   FROM er_dwh.er_procedures epp
     JOIN er_dwh.er_admissions ea ON epp.pomr_id::numeric = ea.visit_id
     JOIN er_lab.lbodr_laborderdetails ll ON epp.patient_order_id = ll.patientorderid
     LEFT JOIN er_lab.lbscl_orderdetails lo ON lo.laborderdetailid = ll.laborderdetailrevisionid
     LEFT JOIN er_lab.lbrst_valuebasedresult lv ON lv.orderdetailid = ll.laborderdetailrevisionid AND lv.testid = lo.testmainid
     LEFT JOIN er_lab.lbrst_textbasedresult lt ON lt.orderdetailid = ll.laborderdetailrevisionid AND lt.testid = lo.testmainid
     LEFT JOIN er_dwh_sub_tables.employees ee ON ee.employee_id = ll.createdby
     LEFT JOIN er_dwh_sub_tables.employees ee1 ON ee1.employee_id = lo.createdby
     LEFT JOIN er_dwh_sub_tables.employees ee2 ON ee2.employee_id = lv.resultedby
     LEFT JOIN er_dwh_sub_tables.employees ee3 ON ee3.employee_id = lt.resultedby
     LEFT JOIN er_dwh_sub_tables.employees ee4 ON ee4.employee_id = lv.primaryverifiedby
     LEFT JOIN er_dwh_sub_tables.employees ee5 ON ee5.employee_id = lt.primaryverifiedby
     LEFT JOIN er_dwh_sub_tables.employees ee6 ON ee6.employee_id = lv.medicalverifiedby
     LEFT JOIN er_dwh_sub_tables.employees ee7 ON ee7.employee_id = lt.medicalverifiedby""")
    
elif st.session_state['page'] == 'er_patient_master':
    render_query_page(
        "Patient Master Data",
        "🛤️",
        """SELECT 
id AS "id",
patientid AS "patientid",
firstname AS "firstname",
middlename AS "middlename",
thirdname AS "thirdname",
lastname AS "lastname",
dateofbirth AS "dateofbirth",
gender AS "gender",
idtype AS "idtype",
idnumber AS "idnumber",
modifiedon as "modifiedon"
FROM er_erfun.erfun_patientdetails epp
WHERE epp.MODIFIED_ON > TO_TIMESTAMP('2024-12-31 23:59:59', 'YYYY-MM-DD HH24:MI:SS')""")
    
elif st.session_state['page'] == 'er_employee_master':
    render_query_page(
        "Employee Master Data",
        "🛤️",
        """SELECT 
employee_id     as "employee_id",
employee_code   as "employee_code",
created_date    as "created_date",
modified_date   as "modified_date",
hospital        as "hospital",
employee_name || ' ' || employee_alias   as "employee_name",
is_active       as "is_active",
is_deleted      as "is_deleted"
FROM RM_RESOURCEREG.RMRRG_EMPLOYEE epp
WHERE epp.modified_date > TO_TIMESTAMP('2024-12-31 23:59:59', 'YYYY-MM-DD HH24:MI:SS')""")

# Add this section at the very end of your existing code, after all the page routing

# Add this section at the very end of your existing code, after the page routing
# Make sure this is at the same indentation level as your other main sections

# Add this section at the very end of your existing code, after the page routing
# Make sure this is at the same indentation level as your other main sections

# ETL Architecture Images Section
if st.session_state['page'] == 'menu':
    # ETL Architecture Images
    st.markdown("---")
    st.markdown("""
    <div class="main-header" style="margin-top: 3rem;">
        <h2>🏗️ ETL Architecture Diagrams</h2>
        <p>Data Warehouse Architecture and Flow Diagrams</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Image 1 - Data Flow Architecture (Lengthy)
    st.markdown("")
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin: 20px 0;">
    """, unsafe_allow_html=True)
    
    st.image("https://raw.githubusercontent.com/Sanjeevaraj-Ethirweerasingham/ER_DWH/main/er_arch11.drawio.png", 
            caption="Source Database to Analytical Database via NiFi Data Ingestion", 
            use_column_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Extra space after lengthy image
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Image 2 - ETL Process Flow (Lengthy)
    st.markdown("####")
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin: 20px 0;">
    """, unsafe_allow_html=True)
    
    st.image("https://raw.githubusercontent.com/Sanjeevaraj-Ethirweerasingham/ER_DWH/main/err_archii_2.drawio.png", 
            caption="Staging Layer and Data Convergence Strategy", 
            use_column_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Extra space after lengthy image
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Image 3 - Data Warehouse Schema (Regular)
    st.markdown("")
    st.image("https://raw.githubusercontent.com/Sanjeevaraj-Ethirweerasingham/ER_DWH/main/err_archi_3drawio.png", 
            caption="Citus Distribution and Business Intelligence", 
            use_column_width=True)
    
    # Regular space
    st.markdown("---")
    
    # Image 4 - Analytics Architecture (Regular)
    st.markdown("")
    st.image("https://raw.githubusercontent.com/Sanjeevaraj-Ethirweerasingham/ER_DWH/main/er_archi_4_.drawio.png", 
            caption="Complete Architecture", 
            use_column_width=True)
