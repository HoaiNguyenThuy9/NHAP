import streamlit as st

# ==============================================================================
# CẤU HÌNH TRANG & CSS NÂNG CAO (CHUẨN UI/UX FINTECH NGÂN HÀNG)
# ==============================================================================
st.set_page_config(page_title="APP CHO VAY ONLINE KHCN - THUY HOAI", layout="wide")

st.markdown("""
    <style>
    /* Nền trang và màu chữ chủ đạo mềm mại */
    .stApp {
        background-color: #f4f7f6;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Thiết kế Banner đỉnh trang */
    .banking-hero {
        background: linear-gradient(135deg, #0a4d3c 0%, #1f8266 100%);
        color: white;
        padding: 40px 50px;
        border-radius: 24px;
        margin-bottom: 35px;
        box-shadow: 0 10px 30px rgba(10, 77, 60, 0.15);
    }
    
    /* Khối Hộp (Card) Chứa các Phân Đoạn */
    .ui-card {
        background: #ffffff;
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 30px;
        border: none;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .ui-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.07);
    }
    
    /* Tiêu đề phân đoạn với điểm nhấn màu xanh */
    .ui-headline {
        color: #0a4d3c;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 25px;
        padding-left: 12px;
        border-left: 5px solid #1f8266;
    }
    
    /* Thiết kế lại các widget nhập liệu của Streamlit cho hiện đại */
    .stTextInput input, .stSelectbox div[data-baseweb="select"], .stNumberInput input {
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        background-color: #f8fafc !important;
        padding: 4px 12px !important;
        color: #334155 !important;
    }
    
    /* Nút bấm Đăng ký phong cách bo góc, đổ bóng (Glow Button) */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #0a4d3c 0%, #1f8266 100%);
        color: white !important;
        border: none;
        padding: 16px 40px;
        font-size: 1.2rem;
        font-weight: 700;
        border-radius: 14px;
        box-shadow: 0 10px 25px rgba(31, 130, 102, 0.3);
        width: 100%;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        margin-top: 15px;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #063328 0%, #155b47 100%);
        box-shadow: 0 12px 30px rgba(31, 130, 102, 0.5);
        transform: scale(1.01);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# THANH SIDEBAR
# ==============================================================================
URL_LOGO = "https://cdn-icons-png.flaticon.com/512/2830/2830284.png"
st.sidebar.image(URL_LOGO, width=100)
st.sidebar.markdown("<h3 style='color:#0a4d3c; margin-top:10px;'>HỆ THỐNG TÍN DỤNG</h3>", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.info("🏢 **Đơn vị thẩm định:** NHÓM 6\n\nHệ thống phê duyệt tự động giảm thời gian xử lý hồ sơ xuống còn 3 giây.")

# ==============================================================================
# BANNER TIÊU ĐỀ ỨNG DỤNG
# ==============================================================================
st.markdown("""
    <div class="banking-hero">
        <h1 style="margin:0; font-size: 2.4rem; font-weight: 800; letter-spacing: -0.5px;">🏦 ĐĂNG KÝ VÀ KIỂM TRA ĐIỀU KIỆN VAY VỐN</h1>
        <p style="margin: 12px 0 0 0; opacity: 0.9; font-size: 1.1rem; font-weight: 300;">
            Hệ thống tự động chấm điểm tín dụng và tính toán dòng tiền chi trả trực tuyến của Khách hàng.
        </p>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# PHẦN 1: ĐỊNH DANH (Bọc trong Hộp giao diện UI)
# ==============================================================================
st.markdown('<div class="ui-card">', unsafe_allow_html=True)
st.markdown('<div class="ui-headline">🪪 1. Xác thực thông tin định danh cá nhân</div>', unsafe_allow_html=True)

col_id1, col_id2, col_id3 = st.columns([1.5, 1.5, 2])
with col_id1:
    ho_ten = st.text_input("Họ và tên chủ hồ sơ:", value="Nguyễn Văn A")
with col_id2:
    cccd = st.text_input("Số Căn cước công dân (12 số):", value="012345678901")
with col_id3:
    dia_chi = st.text_input("Địa chỉ cư trú hiện tại:", value="123 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh")

st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# PHẦN 2 & 3: HAI KHỐI NHẬP LIỆU SONG SONG (LAYOUT GRID CÂN BẰNG)
# ==============================================================================
col_grid1, col_grid2 = st.columns(2)

with col_grid1:
    st.markdown('<div class="ui-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="ui-headline">📋 2. Nhu cầu phân kỳ vay vốn</div>', unsafe_allow_html=True)
    
    danh_sach_loai_vay = [
        "Vay tiêu dùng tín chấp (Không cần tài sản)", 
        "Vay mua Ô tô (Thế chấp bằng xe)", 
        "Vay mua Bất động sản (Thế chấp bằng đất/nhà)", 
        "Vay sản xuất kinh doanh"
    ]
    loai_vay = st.selectbox("Hình thức cấp tín dụng muốn đăng ký:", danh_sach_loai_vay)
    muc_dich = st.text_input("Mục đích sử dụng số tiền cụ thể:", value="Mua nhà chung cư / Chi tiêu gia đình")
    
    STV = st.number_input("Số tiền muốn đề xuất vay (Triệu đồng):", min_value=0.0, value=100.0, step=10.0)
    TGV = st.number_input("Thời gian hoàn trả mong muốn (Số năm):", min_value=0.5, value=5.0, step=0.5)
    LSV = st.number_input("Lãi suất tạm tính (%/năm):", min_value=0.0, max_value=50.0, value=10.0, step=0.5) / 100
    
    if "Không cần tài sản" in loai_vay:
        GTTSDB = 0.0
        st.caption("ℹ️ Hệ thống miễn kê khai tài sản bảo đảm đối với hình thức vay Tín chấp.")
    else:
        GTTSDB = st.number_input("Ước tính giá trị Tài sản thế chấp (Triệu đồng):", min_value=1.0, value=200.0, step=10.0)
    
    danh_sach_tra = [
        "Gốc đều, lãi giảm dần (Kỳ đầu cao nhất, giảm dần về sau)", 
        "Gốc và lãi chia đều cố định hàng tháng (Annuity)"
    ]
    hinh_thuc_tra = st.selectbox("Phương thức trả nợ định kỳ:", danh_sach_tra)
    
    danh_sach_nguon_chinh = [
        "Lương từ công việc cố định (Có HĐLĐ)", 
        "Thu nhập từ hộ kinh doanh / Doanh nghiệp riêng", 
        "Thu nhập từ việc cho thuê tài sản (Nhà, xe)", 
        "Thu nhập tự do không cố định"
    ]
    nguon_chinh = st.selectbox("Nguồn thu nhập chính dùng để trả nợ:", danh_sach_nguon_chinh)
    
    danh_sach_nguon_phu = [
        "Không có", 
        "Thu nhập bổ sung từ Vợ/Chồng", 
        "Tiền gửi tiết kiệm / Tài sản tích lũy khác"
    ]
    nguon_phu = st.selectbox("Nguồn thu nhập bổ sung hỗ trợ:", danh_sach_nguon_phu)
    st.markdown('</div>', unsafe_allow_html=True)

with col_grid2:
    st.markdown('<div class="ui-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="ui-headline">👤 3. Thông tin năng lực tài chính & Lịch sử CIC</div>', unsafe_allow_html=True)
    
    STKH = st.number_input("Số tuổi hiện tại của bạn:", min_value=0, max_value=120, value=30, step=1)
    hon_nhan = st.selectbox("Tình trạng hôn nhân hiện nay:", ["Độc thân", "Đã kết hôn", "Ly hôn/Khác"])
    
    nghe_nghiep_mapping = {
        "Nhân viên văn phòng (HĐLĐ vô thời hạn)": "Nhân viên văn phòng (Có HĐLĐ)",
        "Kinh doanh tự do / Chủ doanh nghiệp": "Chủ cơ sở kinh doanh / Doanh nghiệp",
        "Công chức / Viên chức nhà nước": "Làm việc tại cơ quan Nhà nước",
        "Lao động tự do / Tạm thời": "Lao động tự do / Nghề nghiệp tạm thời"
    }
    nghe_chon = st.selectbox("Công việc/Nghề nghiệp hiện tại:", list(nghe_nghiep_mapping.keys()))
    nghe_nghiep = nghe_nghiep_mapping[nghe_chon]
    
    TN = st.number_input("Tổng thu nhập bình quân tháng (Triệu đồng):", min_value=0.0, value=30.0, step=5.0)
    SNPT = st.number_input("Số người phụ thuộc tài chính trong gia đình:", min_value=0, value=1, step=1)
    PTMC = st.number_input("Số tiền đang phải trả gốc lãi nơi khác hằng tháng (Triệu đồng):", min_value=0.0, value=0.0, step=1.0)
    
    st.markdown("""
        <p style="margin-top:15px; margin-bottom:5px; font-weight:600; color:#0a4d3c;">📊 Lịch sử vay mượn tín dụng cũ:</p>
    """, unsafe_allow_html=True)
    
    danh_sach_no_cu = [
        "Tôi luôn trả nợ đúng hạn / Chưa từng vay mượn ai",
        "Tôi đang có khoản nợ bị quá hạn dưới 90 ngày chưa kịp thanh toán",
        "Tôi đang có nợ quá hạn quá lâu (trên 90 ngày) hoặc đang bị nợ xấu"
    ]
    tinh_trang_no = st.selectbox("Các khoản nợ cũ hiện nay có bị trễ hạn thanh toán không?", danh_sach_no_cu)
    
    if tinh_trang_no == "Tôi luôn trả nợ đúng hạn / Chưa từng vay mượn ai":
        CIC = "Nhóm 1 - Nợ đủ tiêu chuẩn"
    elif tinh_trang_no == "Tôi đang có khoản nợ bị quá hạn dưới 90 ngày chưa kịp thanh toán":
        CIC = "Nhóm 2 - Nợ cần chú ý"
    else:
        CIC = "Nhóm 3 đến 5 - Nợ xấu"

    so_lan_tra_cham = st.number_input("Trong vòng 1 năm qua, số lần nộp chậm/trễ tiền gốc lãi:", min_value=0, value=0, step=1)
    
    if so_lan_tra_cham > 0 or CIC != "Nhóm 1 - Nợ đủ tiêu chuẩn":
        danh_sach_ly_do = [
            "Do sơ xuất, quên ngày thanh toán hoặc do lỗi ứng dụng/lỗi ngân hàng",
            "Do công ty chậm lương, hoặc đối tác thanh toán tiền chậm vài ngày",
            "Do công việc/kinh doanh gặp khó khăn, nguồn thu nhập bị sụt giảm mạnh",
            "Tôi không muốn trả khoản nợ đó hoặc đang có tranh chấp với bên cho vay"
        ]
        ly_do_tra_cham = st.selectbox("Nguyên nhân chính dẫn tới trả chậm:", danh_sach_ly_do)
        
        ly_do_mapping = {
            "Do sơ xuất, quên ngày thanh toán hoặc do lỗi ứng dụng/lỗi ngân hàng": "Lý do khách quan",
            "Do công ty chậm lương, hoặc đối tác thanh toán tiền chậm vài ngày": "Lý do kỹ thuật",
            "Do công việc/kinh doanh gặp khó khăn, nguồn thu nhập bị sụt giảm mạnh": "Lý do chủ quan",
            "Tôi không muốn trả khoản nợ đó hoặc đang có tranh chấp với bên cho vay": "Lý do cố ý"
        }
        ly_do_chuyen_doi = ly_do_mapping[ly_do_tra_cham]
    else:
        ly_do_tra_cham = "Không có trả chậm"
        ly_do_chuyen_doi = "Không có trả chậm"
        
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# KHỐI HIỂN THỊ DÒNG TIỀN ƯỚC TÍNH
# ==============================================================================
TG_Thang = TGV * 12
if TG_Thang > 0:
    Goc_Hang_Thang = STV / TG_Thang
    if "Kỳ đầu cao nhất" in hinh_thuc_tra:
        Lai_Thang_Dau = STV * (LSV / 12)
        PTMM = Goc_Hang_Thang + Lai_Thang_Dau
    else:  
        r_monthly = LSV / 12
        PTMM = STV * (r_monthly * (1 + r_monthly)**TG_Thang) / ((1 + r_monthly)**TG_Thang - 1) if r_monthly > 0 else STV / TG_Thang
else:
    PTMM, Goc_Hang_Thang, Lai_Thang_Dau = 0.0, 0.0, 0.0

st.markdown(f"""
    <div style="background-color: #e6f4f0; border-left: 5px solid #1f8266; padding: 20px; border-radius: 12px; margin: 25px 0;">
        <span style="color: #0a4d3c; font-weight: 700; font-size: 1.1rem;">📊 Dự toán số tiền phải chi trả hàng tháng (Kỳ đầu tiên):</span> 
        <span style="color: #1f8266; font-size: 1.3rem; font-weight: 800;">{PTMM:.2f}</span> Triệu đồng/tháng
        <br><span style="color: #64748b; font-size: 0.9rem;">(Gốc cố định: {Goc_Hang_Thang:.2f} tr | Lãi dự toán tháng thứ nhất: {(PTMM - Goc_Hang_Thang):.2f} tr)</span>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# NÚT GỬI HỒ SƠ & THẨM ĐỊNH KẾT QUẢ
# ==============================================================================
if st.button("📊 Gửi hồ sơ và Kiểm tra kết quả", type="primary"):
    if not ho_ten.strip():
        st.error("❌ Vui lòng cung cấp Họ và Tên chủ hồ sơ.")
    elif len(cccd.strip()) != 12 or not cccd.strip().isdigit():
        st.error("❌ Số CCCD không hợp lệ. Vui lòng kiểm tra lại độ dài 12 chữ số.")
    elif not dia_chi.strip():
        st.error("❌ Vui lòng nhập địa chỉ cư trú để tính toán vùng phân bổ chi nhánh.")
    else:
        try:
            Tong_No_Phai_Tra = PTMM + PTMC
            tong_chi_phi_sinh_hoat = 5.0 + (SNPT * 3.5)
            thu_nhap_rong = TN - tong_chi_phi_sinh_hoat
            DTI = Tong_No_Phai_Tra / TN if TN > 0 else 1.0
            LTV = STV / GTTSDB if GTTSDB > 0 else 0.0
            Tich_Luy_Con_Lai = thu_nhap_rong - PTMM

            # Giao diện hiển thị kết quả đồng bộ
            st.markdown('<div class="ui-card">', unsafe_allow_html=True)
            
            tab1, tab2, tab3 = st.tabs(["📈 Kết quả xét duyệt sơ bộ", "📋 Chi tiết hồ sơ và dòng tiền", "💡 Khuyên dùng từ ngân hàng"])
            
            with tab1:
                st.write(f"### Xin chào Khách hàng: **{ho_ten.upper()}** (CCCD: `{cccd}`)")
                st.write("Các chỉ số an toàn tài chính cá nhân của bạn:")
                m1, m2, m3 = st.columns(3)
                m1.metric(label="Tỷ lệ nợ trên thu nhập (DTI)", value=f"{DTI * 100:.2f}%", delta="Mục tiêu: ≤ 70%")
                if "Không cần tài sản" in loai_vay:
                    m2.metric(label="Tỷ lệ khoản vay trên Tài sản (LTV)", value="Không áp dụng", delta="Vay tín chấp")
                else:
                    m2.metric(label="Tỷ lệ khoản vay trên Tài sản (LTV)", value=f"{LTV * 100:.2f}%", delta="Mục tiêu: ≤ 70%")
                m3.metric(label="Số tuổi của bạn", value=f"{STKH} tuổi", delta="Quy định: 18 - 70 tuổi")
                
                st.markdown("---")
                st.write("### 🏁 KẾT QUẢ ĐÁNH GIÁ TỰ ĐỘNG:")
                
                rejection_reasons = []
                if CIC == "Nhóm 3 đến 5 - Nợ xấu":
                    rejection_reasons.append("Bạn hiện đang có khoản nợ bị quá hạn quá lâu (trên 90 ngày). Ngân hàng không thể cấp thêm khoản vay mới khi nợ cũ chưa giải quyết.")
                if CIC == "Nhóm 2 - Nợ cần chú ý" and ("Lý do chủ quan" in ly_do_chuyen_doi or "Lý do cố ý" in ly_do_chuyen_doi):
                    rejection_reasons.append("Lịch sử trễ hạn cũ xuất phát từ việc kinh doanh khó khăn hoặc tranh chấp, tiềm ẩn rủi ro cho khoản vay mới.")
                elif CIC == "Nhóm 2 - Nợ cần chú ý" and so_lan_tra_cham > 3:
                    rejection_reasons.append(f"Tần suất bạn nộp trễ hạn trong năm qua quá nhiều ({so_lan_tra_cham} lần), cho thấy thói quen tài chính chưa ổn định.")
                if DTI > 0.70:
                    rejection_reasons.append(f"Tổng số tiền trả nợ mỗi tháng chiếm đến {DTI * 100:.2f}% thu nhập của bạn. Áp lực trả nợ quá lớn, vượt ngưỡng an toàn (70%).")
                if "Không cần tài sản" not in loai_vay and LTV > 0.70:
                    rejection_reasons.append(f"Giá trị tài sản bạn thế chấp không đủ bảo đảm cho số tiền muốn vay (Số tiền vay vượt quá 70% giá trị tài sản).")
                if "Không cần tài sản" in loai_vay and STV > 500:
                    rejection_reasons.append("Hạn mức tối đa cho gói vay tín chấp (không tài sản đảm bảo) của khách hàng cá nhân là 500 triệu đồng.")
                if STKH < 18 or STKH > 70:
                    rejection_reasons.append(f"Độ tuổi của bạn ({STKH} tuổi) nằm ngoài khung tuổi quy định hỗ trợ vay vốn (18 đến 70 tuổi).")
                if Tich_Luy_Con_Lai < 0:
                    rejection_reasons.append("Sau khi trừ tiền trả nợ mới và chi phí sinh hoạt tối thiểu của gia đình, thu nhập còn lại của bạn bị âm. Bạn sẽ không đủ tiền chi tiêu.")

                if len(rejection_reasons) == 0:
                    st.success("🎉 **CHÚC MỪNG! HỒ SƠ ĐỦ ĐIỀU KIỆN SƠ TUYỂN (APPROVED)**")
                    st.balloons()
                    st.write(f"Hồ sơ của khách hàng đạt các tiêu chí an toàn cơ bản. Chuyên viên tín dụng ngân hàng tại khu vực sẽ liên hệ với bạn trong thời gian sớm nhất.")
                else:
                    st.error("🚨 **RẤT TIẾC, HỒ SƠ CHƯA ĐỦ ĐIỀU KIỆN (REJECTED)**")
                    st.markdown("**Các lý do khiến hồ sơ chưa đạt:**")
                    for reason in rejection_reasons:
                        st.write(f"- {reason}")
                        
            with tab2:
                st.write("### Chi tiết thông tin đăng ký hồ sơ:")
                st.write(f"- **Họ và tên:** {ho_ten} | **Số CCCD:** `{cccd}`")
                st.write(f"- **Sản phẩm đăng ký:** {loai_vay} | **Mục đích vay:** {muc_dich}")
                st.write(f"- 💵 **Tiền trả định kỳ khoản vay mới này:** `{PTMM:.2f}` Triệu đồng/tháng")
                st.write(f"- 💸 **Ước tính chi phí sinh hoạt tối thiểu gia đình:** `{tong_chi_phi_sinh_hoat:.2f}` Triệu đồng/tháng")
                st.write(f"- 📈 **Số tiền thặng dư còn lại để tích lũy/dự phòng:** `{Tich_Luy_Con_Lai:.2f}` Triệu đồng/tháng")

            with tab3:
                st.write("### Lời khuyên tài chính dành cho bạn:")
                if DTI > 0.50 and DTI <= 0.70:
                    st.warning("⚠️ Khoản nợ này đang chiếm hơn một nửa thu nhập hằng tháng của bạn. Bạn nên cân nhắc kéo dài thời gian vay.")
                if hon_nhan == "Đã kết hôn" and nguon_phu == "Không có":
                    st.warning("⚠️ Bạn nên làm hồ sơ 'Đồng vay' cùng Vợ/Chồng của mình để cộng gộp thu nhập, giúp hồ sơ dễ duyệt hơn.")
                if len(rejection_reasons) == 0 and so_lan_tra_cham == 0:
                    st.write("✅ Bạn có lịch sử tài chính tuyệt vời! Hãy tiếp tục duy trì thói quen chi tiêu đúng hạn này.")
            
            st.markdown('</div>', unsafe_allow_html=True)
                                    
        except ZeroDivisionError:
            st.error("❌ Có lỗi xảy ra trong quá trình tính toán. Vui lòng kiểm tra lại số liệu tài sản hoặc thời gian vay.")
