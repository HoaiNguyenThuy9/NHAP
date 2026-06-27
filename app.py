import streamlit as st

# ==============================================================================
# CẤU HÌNH TRANG WEB & THEME CỦA VIETCOMBANK (UI/UX CHUẨN)
# ==============================================================================
st.set_page_config(page_title="Personal Loans - Vietcombank Style", layout="wide")

# CSS tạo dựng layout phẳng, bo góc nhỏ nhẹ, nút tinh tế và màu xanh Vietcombank (#00a651)
st.markdown("""
    <style>
    /* Nền tổng thể tinh giản trắng/xám mịn */
    .stApp {
        background-color: #fafafa;
        font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Thanh điều hướng giả định phía trên */
    .vcb-nav-sub {
        background-color: #ffffff;
        padding: 12px 20px;
        border-bottom: 1px solid #e1e4e6;
        margin-bottom: 25px;
        border-radius: 8px;
    }
    .vcb-nav-sub span {
        color: #78828a;
        font-size: 0.9rem;
    }
    .vcb-nav-sub strong {
        color: #00a651;
        font-size: 0.9rem;
    }

    /* Tiêu đề trang */
    .vcb-main-title {
        color: #1c2430;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .vcb-sub-title {
        color: #78828a;
        font-size: 1.05rem;
        margin-bottom: 30px;
    }
    
    /* Thiết kế thẻ Card trắng chuẩn Vietcombank */
    .vcb-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 0px; /* Để ảnh tràn viền phía trên */
        margin-bottom: 25px;
        border: 1px solid #eef0f2;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
        overflow: hidden;
    }
    
    /* Phần chứa nội dung padding phía dưới ảnh */
    .vcb-card-body {
        padding: 25px;
    }
    
    /* Tiêu đề trong mỗi Card dịch vụ */
    .vcb-card-header {
        color: #1c2430;
        font-size: 1.25rem;
        font-weight: 600;
        border-left: 4px solid #00a651;
        padding-left: 12px;
        margin-bottom: 20px;
    }
    
    /* Ảnh minh họa của gói sản phẩm */
    .vcb-thumb {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }
    
    /* Định hình lại các ô nhập liệu Streamlit phẳng và thanh mảnh */
    .stTextInput input, .stSelectbox div[data-baseweb="select"], .stNumberInput input {
        border-radius: 6px !important;
        border: 1px solid #dcdfe3 !important;
        background-color: #ffffff !important;
        color: #1c2430 !important;
    }
    
    /* Nút bấm Đăng ký Vay màu xanh lục Vietcombank */
    div.stButton > button:first-child {
        background-color: #00a651;
        color: #ffffff !important;
        border: none;
        padding: 14px 30px;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 6px;
        width: 100%;
        transition: background-color 0.2s ease;
        margin-top: 10px;
    }
    div.stButton > button:first-child:hover {
        background-color: #008741;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar thương hiệu
st.sidebar.markdown("<h2 style='color:#00a651; font-weight:800; text-align:center;'>Vietcombank</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:center; color:#78828a; font-size:0.85rem;'>Chung niềm tin, vững tương lai</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.info("🏢 **Đơn vị phát triển:** NHÓM 6\n\nHệ thống thẩm định dòng tiền tự động dành cho Khách hàng cá nhân.")

# ==============================================================================
# THANH BREADCRUMB (ĐIỀU HƯỚNG PHỤ TRÊN WEBSITE)
# ==============================================================================
st.markdown("""
    <div class="vcb-nav-sub">
        <span>Trang chủ / Khách hàng cá nhân / Sản phẩm dịch vụ / </span><strong>Vay vốn trực tuyến</strong>
    </div>
""", unsafe_allow_html=True)

# Tiêu đề chính trang vay vốn
st.markdown('<h1 class="vcb-main-title">Gói Vay Vốn Khách Hàng Cá Nhân</h1>', unsafe_allow_html=True)
st.markdown('<p class="vcb-sub-title">Vietcombank đồng hành cùng bạn hiện thực hóa các kế hoạch tiêu dùng, mua nhà, mua xe và sản xuất kinh doanh.</p>', unsafe_allow_html=True)

# ==============================================================================
# PHẦN 1: ĐỊNH DANH (Bọc trong Card dịch vụ kèm Ảnh minh họa)
# ==============================================================================
st.markdown("""
    <div class="vcb-card">
        <img class="vcb-thumb" src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&q=80&w=1200" alt="Định danh">
        <div class="vcb-card-body">
            <div class="vcb-card-header">Thông tin khách hàng đăng ký đơn vay</div>
""", unsafe_allow_html=True)

col_id1, col_id2, col_id3 = st.columns([1.5, 1.5, 2])
with col_id1:
    ho_ten = st.text_input("Họ và tên khách hàng:", value="Nguyễn Văn A")
with col_id2:
    cccd = st.text_input("Số CCCD (12 chữ số):", value="012345678901")
with col_id3:
    dia_chi = st.text_input("Địa chỉ cư trú hiện tại (Tỉnh/TP, Quận/Huyện...):", value="123 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh")

st.markdown('</div></div>', unsafe_allow_html=True)

# ==============================================================================
# PHẦN 2 & 3: BỐ CỤC THỂ LAYOUT SONG SONG CÓ HÌNH ẢNH TRONG MỖI THẺ CARD
# ==============================================================================
col_grid1, col_grid2 = st.columns(2)

with col_grid1:
    st.markdown("""
        <div class="vcb-card" style="height: 100%;">
            <img class="vcb-thumb" src="https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&q=80&w=600" alt="Gói vay">
            <div class="vcb-card-body">
                <div class="vcb-card-header">Chi tiết nhu cầu vay vốn</div>
    """, unsafe_allow_html=True)
    
    danh_sach_loai_vay = [
        "Vay tiêu dùng tín chấp (Không cần tài sản)", 
        "Vay mua Ô tô (Thế chấp bằng xe)", 
        "Vay mua Bất động sản (Thế chấp bằng đất/nhà)", 
        "Vay sản xuất kinh doanh"
    ]
    loai_vay = st.selectbox("Sản phẩm cho vay mong muốn:", danh_sach_loai_vay)
    muc_dich = st.text_input("Mục đích sử dụng nguồn vốn giải ngân:", value="Mua nhà chung cư / Chi tiêu gia đình")
    
    STV = st.number_input("Số tiền đề xuất vay vốn (Triệu đồng):", min_value=0.0, value=100.0, step=10.0)
    TGV = st.number_input("Thời gian đăng ký hoàn trả (Số năm):", min_value=0.5, value=5.0, step=0.5)
    LSV = st.number_input("Lãi suất tạm tính (%/năm):", min_value=0.0, max_value=50.0, value=10.0, step=0.5) / 100
    
    if "Không cần tài sản" in loai_vay:
        GTTSDB = 0.0
        st.caption("ℹ️ Gói vay tiêu dùng tín chấp không yêu cầu giá trị tài sản bảo đảm.")
    else:
        GTTSDB = st.number_input("Giá trị ước tính của Tài sản thế chấp (Triệu đồng):", min_value=1.0, value=200.0, step=10.0)
    
    danh_sach_tra = [
        "Gốc đều, lãi giảm dần (Kỳ đầu cao nhất, giảm dần về sau)", 
        "Gốc và lãi chia đều cố định hàng tháng (Annuity)"
    ]
    hinh_thuc_tra = st.selectbox("Phương thức trả nợ gốc và lãi hằng kỳ:", danh_sach_tra)
    
    danh_sach_nguon_chinh = [
        "Lương từ công việc cố định (Có HĐLĐ)", 
        "Thu nhập từ hộ kinh doanh / Doanh nghiệp riêng", 
        "Thu nhập từ việc cho thuê tài sản (Nhà, xe)", 
        "Thu nhập tự do không cố định"
    ]
    nguon_chinh = st.selectbox("Nguồn thu nhập chính chi trả nợ gốc:", danh_sach_nguon_chinh)
    
    danh_sach_nguon_phu = [
        "Không có", 
        "Thu nhập bổ sung từ Vợ/Chồng", 
        "Tiền gửi tiết kiệm / Tài sản tích lũy khác"
    ]
    nguon_phu = st.selectbox("Nguồn thu nhập tích lũy dự phòng:", danh_sach_nguon_phu)
    st.markdown('</div></div>', unsafe_allow_html=True)

with col_grid2:
    st.markdown("""
        <div class="vcb-card" style="height: 100%;">
            <img class="vcb-thumb" src="https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&q=80&w=600" alt="Tài chính">
            <div class="vcb-card-body">
                <div class="vcb-card-header">Năng lực tài chính & Lịch sử tín dụng</div>
    """, unsafe_allow_html=True)
    
    STKH = st.number_input("Số tuổi hiện tại của chủ đơn:", min_value=0, max_value=120, value=30, step=1)
    hon_nhan = st.selectbox("Tình trạng hôn nhân dân sự:", ["Độc thân", "Đã kết hôn", "Ly hôn/Khác"])
    
    nghe_nghiep_mapping = {
        "Nhân viên văn phòng (HĐLĐ vô thời hạn)": "Nhân viên văn phòng (Có HĐLĐ)",
        "Kinh doanh tự do / Chủ doanh nghiệp": "Chủ cơ sở kinh doanh / Doanh nghiệp",
        "Công chức / Viên chức nhà nước": "Làm việc tại cơ quan Nhà nước",
        "Lao động tự do / Tạm thời": "Lao động tự do / Nghề nghiệp tạm thời"
    }
    nghe_chon = st.selectbox("Phân loại nhóm công việc/nghề nghiệp:", list(nghe_nghiep_mapping.keys()))
    nghe_nghiep = nghe_nghiep_mapping[nghe_chon]
    
    TN = st.number_input("Tổng mức thu nhập hằng tháng (Triệu đồng):", min_value=0.0, value=30.0, step=5.0)
    SNPT = st.number_input("Số người đang phụ thuộc kinh tế trực tiếp:", min_value=0, value=1, step=1)
    PTMC = st.number_input("Số tiền đang trả nợ định kỳ ở các TCTD khác (Triệu đồng):", min_value=0.0, value=0.0, step=1.0)
    
    st.markdown("""
        <p style="margin-top:15px; margin-bottom:5px; font-weight:600; color:#1c2430;">Báo cáo quan hệ tín dụng cũ:</p>
    """, unsafe_allow_html=True)
    
    danh_sach_no_cu = [
        "Tôi luôn trả nợ đúng hạn / Chưa từng vay mượn ai",
        "Tôi đang có khoản nợ bị quá hạn dưới 90 ngày chưa kịp thanh toán",
        "Tôi đang có nợ quá hạn quá lâu (trên 90 ngày) hoặc đang bị nợ xấu"
    ]
    tinh_trang_no = st.selectbox("Tình trạng thực tế thanh toán các khoản vay cũ:", danh_sach_no_cu)
    
    if tinh_trang_no == "Tôi luôn trả nợ đúng hạn / Chưa từng vay mượn ai":
        CIC = "Nhóm 1 - Nợ đủ tiêu chuẩn"
    elif tinh_trang_no == "Tôi đang có khoản nợ bị quá hạn dưới 90 ngày chưa kịp thanh toán":
        CIC = "Nhóm 2 - Nợ cần chú ý"
    else:
        CIC = "Nhóm 3 đến 5 - Nợ xấu"

    so_lan_tra_cham = st.number_input("Trong 1 năm qua, số lần phát sinh đóng trễ tiền gốc lãi:", min_value=0, value=0, step=1)
    
    if so_lan_tra_cham > 0 or CIC != "Nhóm 1 - Nợ đủ tiêu chuẩn":
        danh_sach_ly_do = [
            "Do sơ xuất, quên ngày thanh toán hoặc do lỗi ứng dụng/lỗi ngân hàng",
            "Do công ty chậm lương, hoặc đối tác thanh toán tiền chậm vài ngày",
            "Do công việc/kinh doanh gặp khó khăn, nguồn thu nhập bị sụt giảm mạnh",
            "Tôi không muốn trả khoản nợ đó hoặc đang có tranh chấp với bên cho vay"
        ]
        ly_do_tra_cham = st.selectbox("Lý do chính yếu phát sinh chậm trả:", danh_sach_ly_do)
        
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
        
    st.markdown('</div></div>', unsafe_allow_html=True)

# ==============================================================================
# KHỐI HIỂN THỊ DÒNG TIỀN ƯỚC TÍNH SƠ BỘ
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
    <div style="background-color: #f0fbf5; border-left: 4px solid #00a651; padding: 20px; border-radius: 8px; margin: 25px 0;">
        <span style="color: #1c2430; font-weight: 600; font-size: 1.05rem;">📊 Dự tính số tiền đến hạn thanh toán định kỳ (Kỳ thứ 01):</span> 
        <span style="color: #00a651; font-size: 1.3rem; font-weight: 700;">{PTMM:.2f}</span> Triệu đồng/tháng
        <br><span style="color: #78828a; font-size: 0.9rem;">(Trong đó Gốc cố định định kỳ: {Goc_Hang_Thang:.2f} tr | Lãi dự kiến tháng đầu tiên: {(PTMM - Goc_Hang_Thang):.2f} tr)</span>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# NÚT GỬI HỒ SƠ & THẨM ĐỊNH KẾT QUẢ
# ==============================================================================
if st.button("📊 ĐĂNG KÝ VAY VỐN VÀ PHÂN TÍCH HỒ SƠ", type="primary"):
    if not ho_ten.strip():
        st.error("❌ Vui lòng cung cấp Họ và Tên chủ hồ sơ.")
    elif len(cccd.strip()) != 12 or not cccd.strip().isdigit():
        st.error("❌ Số CCCD không hợp lệ (Phải đúng định dạng số bao gồm 12 chữ số).")
    elif not dia_chi.strip():
        st.error("❌ Vui lòng bổ sung thông tin Địa chỉ cư trú.")
    else:
        try:
            Tong_No_Phai_Tra = PTMM + PTMC
            tong_chi_phi_sinh_hoat = 5.0 + (SNPT * 3.5)
            thu_nhap_rong = TN - tong_chi_phi_sinh_hoat
            DTI = Tong_No_Phai_Tra / TN if TN > 0 else 1.0
            LTV = STV / GTTSDB if GTTSDB > 0 else 0.0
            Tich_Luy_Con_Lai = thu_nhap_rong - PTMM

            # Giao diện hiển thị kết quả đồng bộ
            st.markdown('<div class="vcb-card" style="padding:25px;">', unsafe_allow_html=True)
            
            tab1, tab2, tab3 = st.tabs(["📈 Báo cáo phê duyệt sơ bộ", "📋 Phân tích dòng tiền định lượng", "💡 Giải pháp cấu trúc khoản vay"])
            
            with tab1:
                st.write(f"### Kính gửi khách hàng: **{ho_ten.upper()}**")
                m1, m2, m3 = st.columns(3)
                m1.metric(label="Chỉ số nợ trên thu nhập (DTI)", value=f"{DTI * 100:.2f}%", delta="Ngưỡng quy định: ≤ 70%")
                if "Không cần tài sản" in loai_vay:
                    m2.metric(label="Chỉ số đảm bảo khoản vay (LTV)", value="Vay tín chấp", delta="Không yêu cầu tài sản")
                else:
                    m2.metric(label="Chỉ số đảm bảo khoản vay (LTV)", value=f"{LTV * 100:.2f}%", delta="Ngưỡng quy định: ≤ 70%")
                m3.metric(label="Độ tuổi điều kiện", value=f"{STKH} tuổi", delta="Yêu cầu: 18 - 70 tuổi")
                
                st.markdown("---")
                st.write("### 🏁 KẾT LUẬN CỦA HỆ THỐNG PHÊ DUYỆT SỐ:")
                
                rejection_reasons = []
                if CIC == "Nhóm 3 đến 5 - Nợ xấu":
                    rejection_reasons.append("Hồ sơ hiện đang ghi nhận có nợ xấu trên hệ thống trung tâm thông tin tín dụng CIC.")
                if DTI > 0.70:
                    rejection_reasons.append(f"Chỉ số nợ DTI vượt mức trần kiểm soát rủi ro của sản phẩm ({DTI * 100:.2f}%).")
                if STKH < 18 or STKH > 70:
                    rejection_reasons.append(f"Tuổi của quý khách không nằm trong độ tuổi quy định của sản phẩm vay cá nhân.")
                if Tich_Luy_Con_Lai < 0:
                    rejection_reasons.append("Thặng dư tích lũy dòng tiền âm sau khi cân đối chi phí sinh hoạt tối thiểu.")

                if len(rejection_reasons) == 0:
                    st.success("🎉 **CHÚC MỪNG! HỒ SƠ ĐỦ ĐIỀU KIỆN SƠ TUYỂN SỐ THÀNH CÔNG (APPROVED)**")
                    st.balloons()
                else:
                    st.error("🚨 **TỪ CHỐI DUYỆT SƠ BỘ TỰ ĐỘNG (REJECTED)**")
                    st.markdown("**Danh sách tiêu chí chưa đạt chính sách sản phẩm:**")
                    for reason in rejection_reasons:
                        st.write(f"- {reason}")
                        
            with tab2:
                st.write("### Cấu trúc bảng cân đối thu chi hàng tháng:")
                st.write(f"- 💵 **Nghĩa vụ trả gốc lãi khoản vay mới này:** `{PTMM:.2f}` Triệu đồng/tháng")
                st.write(f"- 💳 **Nghĩa vụ trả nợ các khoản tín dụng cũ nơi khác:** `{PTMC:.2f}` Triệu đồng/tháng")
                st.write(f"- 💸 **Hạn mức sinh hoạt gia đình dự kiến:** `{tong_chi_phi_sinh_hoat:.2f}` Triệu đồng/tháng")
                st.write(f"- 📈 **Thặng dư khả dụng tích lũy còn lại:** `{Tich_Luy_Con_Lai:.2f}` Triệu đồng/tháng")

            with tab3:
                st.write("### Khuyến nghị từ phòng quản lý rủi ro bán lẻ:")
                if DTI > 0.50 and DTI <= 0.70:
                    st.warning("⚠️ Áp lực trả nợ hằng kỳ đang lớn. Nên đăng ký kéo dài chu kỳ năm vay để phân bổ nhỏ dòng tiền chi trả.")
                if hon_nhan == "Đã kết hôn" and nguon_phu == "Không có":
                    st.warning("⚠️ Khuyên dùng: Nên chuyển đổi sang hình thức 'Đồng vay' với Vợ/Chồng để tăng xếp hạng tín dụng.")
                if len(rejection_reasons) == 0 and so_lan_tra_cham == 0:
                    st.write("✅ Lịch sử tín dụng và xếp hạng dòng tiền rất tốt. Đề xuất chuyển thẳng hồ sơ sang bộ phận phê duyệt nhanh.")
            
            st.markdown('</div>', unsafe_allow_html=True)
                                    
        except ZeroDivisionError:
            st.error("❌ Có lỗi xảy ra trong quá trình tính toán phân kỳ. Vui lòng kiểm tra lại thông số nhập liệu.")
