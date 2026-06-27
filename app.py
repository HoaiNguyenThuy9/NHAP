import streamlit as st

# ==============================================================================
# CẤU HÌNH TRANG WEB & LOGO (STYLE LUXURY HIGHLIGHT)
# ==============================================================================
st.set_page_config(
    page_title="APP CHO VAY ONLINE KHCN - THUY HOAI", 
    page_icon="👑",
    layout="wide"
)

# NHÚNG MÃ CSS TÙY BIẾN SÂU: HÌNH NỀN ẨN & KHUNG MẢNH SANG TRỌNG
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap');
    
    /* 1. HÌNH NỀN ẨN SANG TRỌNG TOÀN TRANG (MÀU VÀNG NHẸ + HOẠ TIẾT MỜ) */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Montserrat', sans-serif;
        color: #1A2530; /* Chữ màu xanh than đậm quý phái */
        background-color: #FDFBF7; /* Nền trắng ngọc trai ngả vàng nhẹ */
        background-image: 
            linear-gradient(135deg, rgba(244, 239, 227, 0.4) 0%, rgba(253, 251, 247, 0.7) 100%),
            url('https://www.transparenttextures.com/patterns/cream-paper.png'); /* Tạo hiệu ứng vân giấy/vải thô ẩn sang trọng */
        background-attachment: fixed;
    }
    
    /* 2. TÙY BIẾN THANH SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: rgba(244, 239, 227, 0.6);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(197, 160, 89, 0.3);
    }
    
    /* 3. TIÊU ĐỀ CHÍNH */
    .main-title {
        font-family: 'Playfair Display', serif;
        color: #B38E46; /* Vàng đồng Luxury */
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        letter-spacing: 1px;
        margin-bottom: 5px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.02);
    }
    .main-subtitle {
        text-align: center;
        font-style: italic;
        font-weight: 300;
        color: #6A7B8C;
        margin-bottom: 40px;
    }
    
    /* 4. ĐỊNH DẠNG CÁC PHÂN MỤC (SUBHEADER) VỚI ĐƯỜNG KHUNG MẢNH */
    .luxury-subheader {
        font-family: 'Playfair Display', serif;
        color: #1A2530;
        font-size: 1.5rem;
        font-weight: 600;
        border-bottom: 1px solid rgba(197, 160, 89, 0.4); /* Kẻ khung ngang mảnh */
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 25px;
    }
    
    /* 5. ÉP KIỂU KHUNG MẢNH CHO TẤT CẢ Ô NHẬP LIỆU CỦA STREAMLIT (INPUT, SELECTBOX) */
    .stTextInput div[data-baseweb="input"], 
    .stNumberInput div[data-baseweb="input"],
    .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border: 1px solid rgba(197, 160, 89, 0.3) !important; /* Khung viền mỏng vàng nhẹ */
        border-radius: 4px !important;
        transition: all 0.3s ease;
    }
    /* Hiệu ứng khi nhấp chuột vào ô nhập liệu */
    .stTextInput div[data-baseweb="input"]:focus-within, 
    .stNumberInput div[data-baseweb="input"]:focus-within,
    .stSelectbox div[data-baseweb="select"]:focus-within {
        border-color: #B38E46 !important; /* Khung mảnh sáng lên màu vàng đậm */
        box-shadow: 0 0 8px rgba(179, 142, 70, 0.15) !important;
    }
    
    /* 6. HỘP HIỂN THỊ KẾT QUẢ DÒNG TIỀN (RESULT BOX) */
    .result-box {
        background-color: rgba(244, 239, 227, 0.5);
        backdrop-filter: blur(5px);
        padding: 25px;
        border-radius: 6px;
        border: 1px solid rgba(197, 160, 89, 0.4); /* Khung mảnh bao quanh box */
        text-align: center;
        margin-top: 25px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.02);
    }
    .result-amount {
        color: #B38E46;
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: bold;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    
    /* 7. THIẾT KẾ NÚT BẤM CHÍNH (BUTTON) */
    .stButton > button {
        background: linear-gradient(135deg, #C5A059 0%, #B38E46 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        font-weight: 500 !important;
        letter-spacing: 1px !important;
        padding: 12px 30px !important;
        border-radius: 4px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(179, 142, 70, 0.2) !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(179, 142, 70, 0.3) !important;
    }
    
    /* Tùy biến thanh chọn Tabs kết quả */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border: 1px solid rgba(197, 160, 89, 0.2);
        border-bottom: none;
        border-radius: 4px 4px 0 0;
        padding: 8px 24px;
        color: #6A7B8C;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(244, 239, 227, 0.5) !important;
        color: #B38E46 !important;
        border-color: rgba(197, 160, 89, 0.4) !important;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# BỐ CỤC SIDEBAR (THANH ĐIỀU HƯỚNG BÊN TRÁI)
# ==============================================================================
URL_LOGO = "tài chính.png" 
try:
    st.sidebar.image(URL_LOGO, use_container_width=True)
except:
    st.sidebar.markdown("<h2 style='color: #B38E46; text-align:center; font-family: \"Playfair Display\";'>👑 PRIME BANQ</h2>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write("### 🏢 Hệ thống trực tuyến")
st.sidebar.info("Cổng Đăng Ký Khoản Vay Tự Động\n\nTHUY HOAI - NHÓM 6")
st.sidebar.markdown("---")
st.sidebar.caption("Ứng dụng tự động thẩm định hồ sơ đăng ký vay trực tuyến của Khách hàng cá nhân cao cấp.")

# ==============================================================================
# TIÊU ĐỀ CHÍNH (HOMEPAGE HERO)
# ==============================================================================
st.markdown("<div class='main-title'>👑 ĐĂNG KÝ VÀ THẨM ĐỊNH KHOẢN VAY TRỰC TUYẾN</div>", unsafe_allow_html=True)
st.markdown("<div class='main-subtitle'>Hệ thống quản lý tài chính thông minh - Phân tích điều kiện duyệt cấp vốn tự động</div>", unsafe_allow_html=True)

# ==============================================================================
# PHẦN 1: THÔNG TIN ĐỊNH DANH KHÁCH HÀNG
# ==============================================================================
st.markdown("<div class='luxury-subheader'>🪪 1. Xác thực thông tin cá nhân</div>", unsafe_allow_html=True)

col_id1, col_id2, col_id3 = st.columns([1.5, 1.5, 2])
with col_id1:
    ho_ten = st.text_input("Họ và chữ lót, Tên của bạn:", value="Nguyễn Văn A")
with col_id2:
    cccd = st.text_input("Số Căn cước công dân (CCCD - 12 số):", value="012345678901")
with col_id3:
    dia_chi = st.text_input("Địa chỉ cư trú hiện tại (Số nhà, Đường, Tỉnh/TP...):", value="123 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh")

# ==============================================================================
# PHẦN 2 & 3: BỐ CỤC HAI CỘT KHUNG MẢNH TINH TẾ
# ==============================================================================
col_body1, col_body2 = st.columns(2)

with col_body1:
    st.markdown("<div class='luxury-subheader'>📋 2. Nhu cầu phân bổ vốn và Giải pháp</div>", unsafe_allow_html=True)
    
    loai_vay = st.selectbox(
        "Bạn muốn vay theo hình thức nào?", 
        ["Vay tiêu dùng tín chấp (Không cần tài sản)", "Vay mua Ô tô (Thế chấp bằng xe)", "Vay mua Bất động sản (Thế chấp bằng đất/nhà)", "Vay sản xuất kinh doanh"]
    )
    muc_dich = st.text_input("Mục đích sử dụng số tiền này cụ thể là gì?", value="Mua nhà chung cư / Chi tiêu gia đình")
    
    STV = st.number_input("Số tiền bạn muốn vay (Triệu đồng):", min_value=0.0, value=100.0, step=10.0)
    TGV = st.number_input("Thời gian bạn muốn trả góp (Số năm):", min_value=0.5, value=5.0, step=0.5)
    LSV = st.number_input("Lãi suất ước tính (%/năm):", min_value=0.0, max_value=50.0, value=10.0, step=0.5) / 100
    
    if "Không cần tài sản" in loai_vay:
        GTTSDB = 0.0
        st.caption("ℹ️ Hệ thống ghi nhận: Gói vay tín chấp đặc quyền không yêu cầu tài sản đảm bảo.")
    else:
        GTTSDB = st.number_input("Ước tính giá trị Tài sản bạn định thế chấp (Triệu đồng):", min_value=1.0, value=200.0, step=10.0)
    
    hinh_thuc_tra = st.selectbox(
        "Bạn muốn trả nợ theo phương thức nào?", 
        ["Gốc đều, lãi giảm dần (Kỳ đầu cao nhất, giảm dần về sau)", "Gốc và lãi chia đều cố định hàng tháng (Annuity)"]
    )
    nguon_chinh = st.selectbox(
        "Nguồn thu nhập chính để bạn trả nợ từ đâu?", 
        ["Lương từ công việc cố định (Có HĐLĐ)", "Thu nhập từ hộ kinh doanh / Doanh nghiệp riêng", "Thu nhập từ việc cho thuê tài sản (Nhà, xe)", "Thu nhập tự do không cố định"]
    )
    nguon_phu = st.selectbox(
        "Bạn có nguồn thu nhập dự phòng nào khác không?", 
        ["Không có", "Thu nhập bổ sung từ Vợ/Chồng", "Tiền gửi tiết kiệm / Tài sản tích lũy khác"]
    )

with col_body2:
    st.markdown("<div class='luxury-subheader'>👤 3. Định biên tài chính và Lịch sử CIC</div>", unsafe_allow_html=True)
    
    STKH = st.number_input("Số tuổi hiện tại của bạn (Tuổi):", min_value=0, max_value=120, value=30, step=1)
    hon_nhan = st.selectbox("Tình trạng hôn nhân hiện tại:", ["Độc thân", "Đã kết hôn", "Ly hôn/Khác"])
    
    nghe_nghiep_mapping = {
        "Nhân viên văn phòng (HĐLĐ vô thời hạn)": "Nhân viên văn phòng (Có HĐLĐ)",
        "Kinh doanh tự do / Chủ doanh nghiệp": "Chủ cơ sở kinh doanh / Doanh nghiệp",
        "Công chức / Viên chức nhà nước": "Làm việc tại cơ quan Nhà nước",
        "Lao động tự do / Tạm thời": "Lao động tự do / Nghề nghiệp tạm thời"
    }
    nghe_chon = st.selectbox("Công việc hiện tại của bạn:", list(nghe_nghiep_mapping.keys()))
    nghe_nghiep = nghe_nghiep_mapping[nghe_chon]
    
    TN = st.number_input("Tổng thu nhập hàng tháng của bạn (Triệu đồng):", min_value=0.0, value=30.0, step=5.0)
    SNPT = st.number_input("Số người bạn đang nuôi nấng/phụ thuộc trong gia đình (Người):", min_value=0, value=1, step=1)
    PTMC = st.number_input("Số tiền bạn đang phải trả nợ hàng tháng cho các tổ chức khác (Triệu đồng):", min_value=0.0, value=0.0, step=1.0)
    
    st.markdown("<p style='font-weight: 500; margin-bottom: 5px;'>📌 Lịch sử vay mượn & Trả nợ cũ:</p>", unsafe_allow_html=True)
    tinh_trang_no = st.selectbox(
        "Hiện tại, các khoản vay cũ của bạn tại các ngân hàng có từng bị trễ hạn không?",
        [
            "Tôi luôn trả nợ đúng hạn / Chưa từng vay mượn ai",
            "Tôi đang có khoản nợ bị quá hạn dưới 90 ngày chưa kịp thanh toán",
            "Tôi đang có nợ quá hạn quá lâu (trên 90 ngày) hoặc đang bị nợ xấu"
        ]
    )
    
    if tinh_trang_no == "Tôi luôn trả nợ đúng hạn / Chưa từng vay mượn ai":
        CIC = "Nhóm 1 - Nợ đủ tiêu chuẩn"
    elif tinh_trang_no == "Tôi đang có khoản nợ bị quá hạn dưới 90 ngày chưa kịp thanh toán":
        CIC = "Nhóm 2 - Nợ cần chú ý"
    else:
        CIC = "Nhóm 3 đến 5 - Nợ xấu"

    so_lan_tra_cham = st.number_input(
        "Trong vòng 1 năm qua, bạn đã từng đóng tiền trễ hạn bao nhiêu lần?", 
        min_value=0, value=0, step=1
    )
    
    ly_do_tra_cham = "Không có trả chậm"
    if so_lan_tra_cham > 0 or CIC != "Nhóm 1 - Nợ đủ tiêu chuẩn":
        ly_do_tra_cham = st.selectbox(
            "Nguyên nhân chính dẫn đến việc chậm thanh toán kỳ trước:",
            [
                "Do sơ xuất, quên ngày thanh toán hoặc do lỗi ứng dụng/lỗi ngân hàng",
                "Do công ty chậm lương, hoặc đối tác thanh toán tiền chậm vài ngày",
                "Do công việc/kinh doanh gặp khó khăn, nguồn thu nhập bị sụt giảm mạnh",
                "Tôi không muốn trả khoản nợ đó hoặc đang có tranh chấp với bên cho vay"
            ]
        )
        ly_do_mapping = {
            "Do sơ xuất, quên ngày thanh toán hoặc do lỗi ứng dụng/lỗi ngân hàng": "Lý do khách quan",
            "Do công ty chậm lương, hoặc đối tác thanh toán tiền chậm vài ngày": "Lý do kỹ thuật",
            "Do công việc/kinh doanh gặp khó khăn, nguồn thu nhập bị sụt giảm mạnh": "Lý do chủ quan",
            "Tôi không muốn trả khoản nợ đó hoặc đang có tranh chấp với bên cho vay": "Lý do cố ý"
        }
        ly_do_chuyen_doi = ly_do_mapping[ly_do_tra_cham]
    else:
        ly_do_chuyen_doi = "Không có trả chậm"

# ==============================================================================
# HỘP ƯỚC TÍNH ĐÒNG TIỀN REAL-TIME (KHUNG MẢNH VÀNG NHẸ)
# ==============================================================================
TG_Thang = TGV * 12
if TG_Thang > 0:
    Goc_Hang_Thang = STV / TG_Thang
    if "Kỳ đầu cao nhất" in hinh_thuc_tra:
        Lai_Thang_Dau = STV * (LSV / 12)
        PTMM = Goc_Hang_Thang + Lai_Thang_Dau
    else:  
        r_monthly = LSV / 12
        if r_monthly > 0:
            PTMM = STV * (r_monthly * (1 + r_monthly)**TG_Thang) / ((1 + r_monthly)**TG_Thang - 1)
        else:
            PTMM = STV / TG_Thang
else:
    PTMM = 0.0
    Goc_Hang_Thang = 0.0
    Lai_Thang_Dau = 0.0

st.markdown(f"""
    <div class="result-box">
        <p style="margin: 0; color: #6A7B8C; font-size: 0.95rem; font-weight: 500; letter-spacing: 0.5px;">💡 ƯỚC TÍNH NGHĨA VỤ HOÀN TRẢ ĐỊNH KỲ (KỲ ĐẦU TIÊN)</p>
        <p class="result-amount">{PTMM:.2f} Triệu VND / tháng</p>
        <p style="margin: 0; color: #8A9AAB; font-size: 0.85rem; font-style: italic;">
            (Tiền Gốc: {Goc_Hang_Thang:.2f} tr | Tiền Lãi tháng đầu: {PTMM - Goc_Hang_Thang:.2f} tr — Tính trên mức lãi suất ước tính {LSV*100:.1f}%/năm)
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==============================================================================
# NÚT GỬI HỒ SƠ & THẨM ĐỊNH TỰ ĐỘNG
# ==============================================================================
if st.button("📊 KÍCH HOẠT THẨM ĐỊNH & XEM KẾT QUẢ", type="primary", use_container_width=True):
    
    if not ho_ten.strip():
        st.error("❌ Hệ thống yêu cầu: Vui lòng nhập đầy đủ Họ và Tên chủ hồ sơ.")
    elif len(cccd.strip()) != 12 or not cccd.strip().isdigit():
        st.error("❌ Định dạng không đúng: Số CCCD bắt buộc phải là 12 ký tự số.")
    elif not dia_chi.strip():
        st.error("❌ Hệ thống yêu cầu: Cung cấp địa chỉ cư trú hiện tại để phân vùng chi nhánh.")
    else:
        try:
            # Quy đổi dòng tiền quản trị ngân hàng
            Tong_No_Phai_Tra = PTMM + PTMC
            CPSH_BAN_THAN = 5.0
            CPSH_PHU_THUOC = 3.5
            tong_chi_phi_sinh_hoat = CPSH_BAN_THAN + (SNPT * CPSH_PHU_THUOC)
            thu_nhap_rong = TN - tong_chi_phi_sinh_hoat
            
            DTI = Tong_No_Phai_Tra / TN if TN > 0 else 1.0
            LTV = STV / GTTSDB if GTTSDB > 0 else 0.0
            Tich_Luy_Con_Lai = thu_nhap_rong - PTMM

            # Chia Tab hiển thị kết quả xử lý
            tab1, tab2, tab3 = st.tabs(["📈 Kết quả xét duyệt sơ bộ", "📋 Chi tiết hồ sơ và dòng tiền", "💡 Khuyên dùng từ ngân hàng"])
            
            with tab1:
                st.markdown(f"### Kính gửi Khách hàng: **{ho_ten.upper()}** (Mã định danh bảo mật: `{cccd}`)")
                st.write("Bản phân tích chỉ số rủi ro an toàn tài chính cá nhân:")
                m1, m2, m3 = st.columns(3)
                m1.metric(label="Tỷ lệ nợ trên thu nhập (DTI)", value=f"{DTI * 100:.2f}%", delta="Ngưỡng an toàn: ≤ 70%")
                if "Không cần tài sản" in loai_vay:
                    m2.metric(label="Tỷ lệ khoản vay trên Tài sản (LTV)", value="Không áp dụng", delta="Hạn mức tín chấp")
                else:
                    m2.metric(label="Tỷ lệ khoản vay trên Tài sản (LTV)", value=f"{LTV * 100:.2f}%", delta="Hạn mức thế chấp: ≤ 70%")
                m3.metric(label="Độ tuổi phân lớp", value=f"{STKH} tuổi", delta="Khung quy định: 18 - 70 tuổi")
                
                st.markdown("---")
                st.write("### 🏁 KẾT LUẬN CỦA HỆ THỐNG CHẤM ĐIỂM TỰ ĐỘNG:")
                
                rejection_reasons = []
                
                # Luật CIC chặn cứng
                if CIC == "Nhóm 3 đến 5 - Nợ xấu":
                    rejection_reasons.append("Hệ thống ghi nhận bạn đang có nợ xấu hoặc quá hạn trên 90 ngày tại tổ chức khác. Ngân hàng từ chối cấp hạn mức mới.")
                if CIC == "Nhóm 2 - Nợ cần chú ý":
                    if "Lý do chủ quan" in ly_do_chuyen_doi or "Lý do cố ý" in ly_do_chuyen_doi:
                        rejection_reasons.append("Lịch sử thanh toán chậm do lý do chủ quan hoặc tranh chấp, rủi ro xếp hạng tín dụng cao.")
                    elif so_lan_tra_cham > 3:
                        rejection_reasons.append(f"Tần suất chậm đóng kỳ hạn cũ quá cao ({so_lan_tra_cham} lần trong năm), hồ sơ không đạt chuẩn uy tín dòng tiền.")
                if "Lý do cố ý" in ly_do_chuyen_doi:
                    rejection_reasons.append("Từ chối tự động do ghi nhận khách hàng cố ý không hoàn trả nợ cũ.")
                if CIC == "Nhóm 1 - Nợ đủ tiêu chuẩn" and so_lan_tra_cham > 5:
                    rejection_reasons.append(f"Mật độ đóng trễ hạn kỹ thuật quá nhiều ({so_lan_tra_cham} lần), điểm uy tín hệ thống dưới mức trung bình.")

                # Luật Tài chính chặn cứng
                if DTI > 0.70:
                    rejection_reasons.append(f"Chỉ số DTI đạt {DTI * 100:.2f}%. Áp lực trả nợ vượt quá 70% tổng thu nhập hàng tháng, vượt mức kiểm soát rủi ro.")
                if "Không cần tài sản" not in loai_vay and LTV > 0.70:
                    rejection_reasons.append(f"Giá trị tài sản bảo đảm (LTV = {LTV * 100:.2f}%) không đủ tỷ lệ bao phủ an toàn cho khoản vay muốn giải ngân.")
                if "Không cần tài sản" in loai_vay and STV > 500:
                    rejection_reasons.append("Vượt hạn mức tối đa quy định cho dòng sản phẩm vay tiêu dùng tín chấp cá nhân (Tối đa 500 triệu đồng).")
                if STKH < 18 or STKH > 70:
                    rejection_reasons.append(f"Độ tuổi hiện tại ({STKH} tuổi) nằm ngoài phạm vi chịu trách nhiệm dân sự/quy định cấp vốn vay (18 - 70 tuổi).")
                if Tich_Luy_Con_Lai < 0:
                    rejection_reasons.append("Dòng tiền thặng dư hàng tháng sau khi trừ sinh hoạt phí tối thiểu và tiền gốc lãi bị âm. Khách hàng không đủ khả năng duy trì cuộc sống.")
                if "Lao động tự do" in nghe_nghiep and "Không cần tài sản" in loai_vay:
                    rejection_reasons.append("Gói sản phẩm tín chấp yêu cầu bắt buộc chứng minh nguồn thu nhập ổn định từ lương có Hợp đồng lao động cố định.")

                if len(rejection_reasons) == 0:
                    st.success("🎉 **CHÚC MỪNG! HỒ SƠ ĐỦ ĐIỀU KIỆN PHÊ DUYỆT SƠ BỘ (APPROVED)**")
                    st.balloons()
                    st.write(f"Hồ sơ của khách hàng **{ho_ten}** đã thông qua các bộ lọc rủi ro an toàn tự động. Giám đốc quản lý phân khúc cấp cao tại chi nhánh phụ trách khu vực **{dia_chi}** sẽ liên hệ thiết lập lịch hẹn nộp hồ sơ giấy trong vòng 15 phút.")
                else:
                    st.error("🚨 **RẤT TIẾC, HỒ SƠ CHƯA ĐỦ ĐIỀU KIỆN CẤP VỐN (REJECTED)**")
                    st.markdown("**Danh mục các tiêu chí chưa đạt chuẩn hệ thống:**")
                    for reason in rejection_reasons:
                        st.write(f"- {reason}")
                        
            with tab2:
                st.write("### Chi tiết dữ liệu đăng ký phân tích:")
                c_info1, c_info2 = st.columns(2)
                with c_info1:
                    st.write(f"- **Họ và tên chủ hộ:** {ho_ten}")
                    st.write(f"- **Mã số định danh:** `{cccd}`")
                    st.write(f"- **Khu vực cư trú:** {dia_chi}")
                    st.write(f"- **Sản phẩm yêu cầu:** {loai_vay}")
                    st.write(f"- **Mục đích giải ngân:** {muc_dich}")
                with c_info2:
                    st.write(f"- **Tình trạng gia cảnh:** {hon_nhan}")
                    st.write(f"- **Phân loại ngành nghề:** {nghe_chon}")
                    st.write(f"- **Phân loại lịch sử tín dụng:** {tinh_trang_no} (Ghi nhận đóng trễ {so_lan_tra_cham} lần)")
                    st.write(f"- **Bản chất nguyên nhân chậm trả (nếu có):** {ly_do_tra_cham}")

                st.markdown("---")
                st.write("### Tóm tắt kiểm toán dòng tiền cá nhân hàng tháng:")
                st.write(f"- 💵 **Nghĩa vụ hoàn trả định kỳ cho khoản vay mới:** `{PTMM:.2f}` Triệu đồng/tháng")
                st.write(f"- 💳 **Chi phí trả nợ cũ tại các tổ chức tín dụng khác:** `{PTMC:.2f}` Triệu đồng/tháng")
                st.write(f"- 💸 **Định mức chi phí ăn ở, sinh hoạt tối thiểu của gia đình:** `{tong_chi_phi_sinh_hoat:.2f}` Triệu đồng/tháng")
                st.write(f"- 📈 **Dòng tiền thặng dư còn lại để dự phòng tích lũy:** `{Tich_Luy_Con_Lai:.2f}` Triệu đồng/tháng")

            with tab3:
                st.write("### Khuyến nghị tư vấn cấu trúc tài chính từ chuyên gia:")
                if DTI > 0.50 and DTI <= 0.70:
                    st.warning("⚠️ Cảnh báo: Tỷ lệ trả nợ đang chiếm tỷ trọng lớn trong thu nhập. Khuyến nghị cấu trúc lại thời gian vay dài hơn (tăng số năm trả góp) nhằm giảm áp lực dòng tiền hàng tháng.")
                if "Lý do khách quan" in ly_do_chuyen_doi:
                    st.info("ℹ️ Giải pháp: Để tối ưu điểm tín dụng, sau khi được giải ngân, quý khách nên đăng ký tính năng 'Trích nợ tự động - Auto Debit' trên ví/app ngân hàng để tránh sai sót quên ngày.")
                if "Lý do kỹ thuật" in ly_do_chuyen_doi:
                    st.info("ℹ️ Giải pháp: Quý khách có quyền yêu cầu chuyên viên tín dụng điều chỉnh ngày đến hạn thanh toán hàng tháng trùng với ngày nhận lương định kỳ của cơ quan.")
                if hon_nhan == "Đã kết hôn" and nguon_phu == "Không có":
                    st.warning("⚠️ Khuyến nghị: Quý khách nên bổ sung hồ sơ theo phương thức 'Đồng vay' (vợ/chồng cùng ký) nhằm cộng gộp tổng thu nhập gia đình, giúp gia tăng đáng kể điểm số phê duyệt.")
                if len(rejection_reasons) == 0 and so_lan_tra_cham == 0:
                    st.write("✅ Đánh giá: Quý khách sở hữu lịch sử quản lý tài chính vô cùng xuất sắc! Hãy tiếp tục duy trì thói quen chi tiêu thông minh này.")
                                    
        except ZeroDivisionError:
            st.error("❌ Lỗi hệ thống: Vui lòng kiểm tra lại thông số nhập liệu (Giá trị tài sản đảm bảo hoặc thời hạn vay phải lớn hơn 0).")

# ==============================================================================
# CHÂN TRANG (FOOTER CAO CẤP)
# ==============================================================================
st.markdown("<br><hr><p style='text-align: center; color: #8A9AAB; font-size: 0.85rem; letter-spacing: 0.5px;'>© 2026 Hệ thống thẩm định và quản trị rủi ro tài chính cá nhân cao cấp. Hệ thống bảo lưu mọi quyền.</p>", unsafe_allow_html=True)
