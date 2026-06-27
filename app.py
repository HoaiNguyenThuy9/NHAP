Để đưa giao diện ứng dụng vay trực tuyến của bạn lên một đẳng cấp hoàn toàn khác—chuyên nghiệp, sang trọng và giống một ứng dụng ngân hàng số thực tế nhất—chúng ta sẽ áp dụng ngôn ngữ thiết kế Neumorphism kết hợp Card lướt hình ảnh theo đúng chuẩn UI/UX của các ứng dụng tài chính cao cấp (như hình mẫu Vietcombank bạn hướng tới).

Dưới đây là phiên bản mã nguồn đã được làm lại toàn bộ phần nhìn, tối ưu hóa các thẻ nhập liệu thành các khối hộp bo góc mềm mại, đổ bóng nổi 3D, tích hợp biểu tượng thanh lịch và tạo các khu vực nhập liệu vô cùng scannable (dễ quét mắt).

🏦 Mã nguồn Streamlit Giao diện Ngân hàng Số Đẳng cấp
Python
import streamlit as st

# ==============================================================================
# CẤU HÌNH TRANG WEB & TOÀN BỘ CSS CAO CẤP (CUSTOM PREMIUM UI)
# ==============================================================================
st.set_page_config(page_title="APP CHO VAY ONLINE KHCN - THUY HOAI", layout="wide")

st.markdown("""
    <style>
    /* 1. Thiết lập nền trang và font chữ thanh lịch */
    .stApp {
        background-color: #f3f6f9;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* 2. Banner chính dạng khối bo góc lớn với dải màu tài chính */
    .premium-hero {
        background: linear-gradient(135deg, #0f5132 0%, #198754 100%);
        color: white;
        padding: 40px;
        border-radius: 24px;
        margin-bottom: 35px;
        box-shadow: 0 12px 30px rgba(25, 135, 84, 0.2);
    }
    
    /* 3. Khung Card 3D cao cấp cho các mục nhập liệu 1, 2, 3 */
    .banking-card {
        background: #ffffff;
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 30px;
        border: 1px solid rgba(0,0,0,0.03);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.03), 0 2px 5px rgba(0, 0, 0, 0.02);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .banking-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.06);
    }
    
    /* 4. Tiêu đề các mục được trang trí dải màu */
    .card-headline {
        color: #0f5132;
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid #e9ecef;
        display: flex;
        align-items: center;
    }
    
    /* 5. Định hình lại các Widget của Streamlit (Ô nhập liệu, Hộp chọn) */
    .stTextInput div[data-baseweb="input"], .stSelectbox div[data-baseweb="select"], .stNumberInput div[data-baseweb="input"] {
        border-radius: 10px !important;
        border: 1px solid #ced4da !important;
        background-color: #f8f9fa !important;
    }
    
    /* 6. Thiết kế nút bấm "Gửi hồ sơ" chuẩn phong cách App Mobile */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #115e3b 0%, #198754 100%);
        color: white !important;
        border: none;
        padding: 16px 35px;
        font-size: 1.2rem;
        font-weight: 700;
        border-radius: 14px;
        box-shadow: 0 8px 20px rgba(25, 135, 84, 0.3);
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #0a3620 0%, #146c43 100%);
        box-shadow: 0 12px 25px rgba(25, 135, 84, 0.4);
        transform: translateY(-1px);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# THANH SIDEBAR THƯƠNG HIỆU
# ==============================================================================
URL_LOGO = "tài chính.png" 
try:
    st.sidebar.image(URL_LOGO, use_container_width=True)
except:
    st.sidebar.markdown("<h2 style='color:#198754; text-align:center;'>🏦 KHCN LOAN</h2>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏢 Hệ thống trực tuyến")
st.sidebar.info("✨ **Cổng Đăng Ký Khoản Vay Tự Động**\n\nPhát triển bởi: **NHÓM 6**")
st.sidebar.caption("Ứng dụng tự động thẩm định hồ sơ đăng ký vay trực tuyến của Khách hàng cắt giảm 90% thời gian chờ đợi.")

# ==============================================================================
# ĐỈNH TRANG: HERO BANNER SANG TRỌNG
# ==============================================================================
st.markdown("""
    <div class="premium-hero">
        <h1 style="margin:0; font-size: 2.3rem; font-weight: 800; letter-spacing: -0.5px;">🏦 ĐĂNG KÝ VÀ KIỂM TRA ĐIỀU KIỆN VAY TRỰC TUYẾN</h1>
        <p style="margin: 10px 0 0 0; opacity: 0.9; font-size: 1.1rem; font-weight: 300;">
            Hệ thống quản trị rủi ro tự động thông minh. Vui lòng cung cấp chính xác dòng tiền để nhận kết quả phê duyệt sau 3 giây.
        </p>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# PHẦN 1: THÔNG TIN ĐỊNH DANH (Bọc trong Card trắng viền bo mờ)
# ==============================================================================
st.markdown('<div class="banking-card">', unsafe_allow_html=True)
st.markdown('<div class="card-headline">🪪 &nbsp; 1. Thông tin định danh cá nhân chính chủ</div>', unsafe_allow_html=True)

col_id1, col_id2, col_id3 = st.columns([1.5, 1.5, 2])
with col_id1:
    ho_ten = st.text_input("Họ và tên khách hàng (In hoa):", value="Nguyễn Văn A")
with col_id2:
    cccd = st.text_input("Số Căn cước công dân (12 chữ số):", value="012345678901")
with col_id3:
    dia_chi = st.text_input("Địa chỉ nơi ở / Cư trú hiện tại:", value="123 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh")

st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# PHẦN 2 & 3: PHÂN TÁCH HAI KHỐI TÀI CHÍNH SONG SONG CHUẨN GRID
# ==============================================================================
col_grid1, col_grid2 = st.columns(2)

with col_grid1:
    st.markdown('<div class="banking-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="card-headline">📋 &nbsp; 2. Thiết lập thông số nhu cầu vay vốn</div>', unsafe_allow_html=True)
    
    loai_vay = st.selectbox(
        "Lựa chọn sản phẩm vay tín dụng:", 
        ["Vay tiêu dùng tín chấp (Không cần tài sản)", "Vay mua Ô tô (Thế chấp bằng xe)", "Vay mua Bất động sản (Thế chấp bằng đất/nhà)", "Vay sản xuất kinh doanh"]
    )
    muc_dich = st.text_input("Mục đích sử dụng vốn giải ngân thực tế:", value="Mua nhà chung cư / Chi tiêu gia đình")
    
    STV = st.number_input("Số tiền đề xuất vay (Triệu đồng):", min_value=0.0, value=100.0, step=10.0)
    TGV = st.number_input("Thời gian đăng ký hoàn trả (Số năm):", min_value=0.5, value=5.0, step=0.5)
    LSV = st.number_input("Lãi suất giả định áp dụng (%/năm):", min_value=0.0, max_value=50.0, value=10.0, step=0.5) / 100
    
    if "Không cần tài sản" in loai_vay:
        GTTSDB = 0.0
        st.markdown("<small style='color: #6c757d;'>ℹ️ Hệ thống tự động miễn kê khai Tài sản bảo đảm cho gói Tín chấp.</small>", unsafe_allow_html=True)
    else:
        GTTSDB = st.number_input("Giá trị thị trường của Tài sản thế chấp (Triệu đồng):", min_value=1.0, value=200.0, step=10.0)
        
    hinh_thuc_tra = st.selectbox(
        "Phương án thanh toán kỳ gốc và lãi:", 
        ["Gốc đều, lãi giảm dần (Kỳ đầu cao nhất, giảm dần về sau)", "Gốc và lãi chia đều cố định hàng tháng (Annuity)"]
    )
    nguon_chinh = st.selectbox(
        "Nguồn thu nhập chi trả gốc chính:", 
        ["Lương từ công việc cố định (Có HĐLĐ)", "Thu nhập từ hộ kinh doanh / Doanh nghiệp riêng", "Thu nhập từ việc cho thuê tài sản (Nhà, xe)", "Thu nhập tự do không cố định"]
    )
    nguon_phu = st.selectbox(
        "Nguồn thu nhập đồng hành/Dự phòng:", 
        ["Không có", "Thu nhập bổ sung từ Vợ/Chồng", "Tiền gửi tiết kiệm / Tài sản tích lũy khác"]
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col_grid2:
    st.markdown('<div class="banking-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="card-headline">👤 &nbsp; 3. Năng lực tài chính & Lịch sử tín dụng CIC</div>', unsafe_allow_html=True)
    
    STKH = st.number_input("Độ tuổi hiện tại của chủ đơn (Tuổi):", min_value=0, max_value=120, value=30, step=1)
    hon_nhan = st.selectbox("Tình trạng hôn nhân dân sự:", ["Độc thân", "Đã kết hôn", "Ly hôn/Khác"])
    
    nghe_nghiep_mapping = {
        "Nhân viên văn phòng (HĐLĐ vô thời hạn)": "Nhân viên văn phòng (Có HĐLĐ)",
        "Kinh doanh tự do / Chủ doanh nghiệp": "Chủ cơ sở kinh doanh / Doanh nghiệp",
        "Công chức / Viên chức nhà nước": "Làm việc tại cơ quan Nhà nước",
        "Lao động tự do / Tạm thời": "Lao động tự do / Nghề nghiệp tạm thời"
    }
    nghe_chon = st.selectbox("Lĩnh vực ngành nghề công việc hiện tại:", list(nghe_nghiep_mapping.keys()))
    nghe_nghiep = nghe_nghiep_mapping[nghe_chon]
    
    TN = st.number_input("Tổng mức thu nhập thực tế hàng tháng (Triệu đồng):", min_value=0.0, value=30.0, step=5.0)
    SNPT = st.number_input("Số nhân khẩu đang phụ thuộc tài chính (Người):", min_value=0, value=1, step=1)
    PTMC = st.number_input("Số tiền đang trả nợ định kỳ tại các Ngân hàng khác (Triệu đồng):", min_value=0.0, value=0.0, step=1.0)
    
    st.markdown("<p style='margin-top:15px; margin-bottom:5px; font-weight:600; color:#212529;'>📊 Tình trạng quan hệ tín dụng cũ:</p>", unsafe_allow_html=True)
    tinh_trang_no = st.selectbox(
        "Các khoản vay cũ hoặc dư nợ thẻ tín dụng hiện tại có trễ hạn không?",
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
        "Số lần phát sinh trả chậm/quên đóng tiền trong 12 tháng gần nhất:", 
        min_value=0, value=0, step=1
    )
    
    if so_lan_tra_cham > 0 or CIC != "Nhóm 1 - Nợ đủ tiêu chuẩn":
        ly_do_tra_cham = st.selectbox(
            "Lý do cốt lõi của việc thanh toán chậm trễ:",
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
        ly_do_tra_cham = "Không có trả chậm"
        ly_do_chuyen_doi = "Không có trả chậm"
        
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# PHẦN TOÁN DÒNG TIỀN REAL-TIME KỲ ĐẦU
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
    <div style="background-color: #e8f5e9; border-left: 5px solid #2e7d32; padding: 20px; border-radius: 12px; margin: 25px 0; box-shadow: 0 4px 12px rgba(46,125,50,0.06);">
        <strong style="color: #1b5e20; font-size:1.1rem;">📊 Dự toán nghĩa vụ thanh toán định kỳ (Kỳ thứ 01):</strong> 
        <span style="color: #2e7d32; font-size: 1.3rem; font-weight: 800;">{PTMM:.2f}</span> Triệu đồng/tháng 
        <br><span style="color: #555; font-size:0.9rem;">(Trong đó gồm Gốc cố định: <b>{Goc_Hang_Thang:.2f} tr</b> và Lãi dự kiến tháng đầu: <b>{PTMM - Goc_Hang_Thang:.2f} tr</b>)</span>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# PHẦN 4: HÀNH ĐỘNG GỬI DUYỆT & TRẢ KẾT QUẢ TỰ ĐỘNG
# ==============================================================================
if st.button("📊 Khởi chạy thẩm định & Xem kết quả", type="primary"):
    if not ho_ten.strip():
        st.error("❌ Hệ thống yêu cầu cung cấp Họ và Tên để tra cứu CIC.")
    elif len(cccd.strip()) != 12 or not cccd.strip().isdigit():
        st.error("❌ Định dạng Căn cước công dân không chính xác (Phải đủ 12 ký tự số).")
    elif not dia_chi.strip():
        st.error("❌ Vui lòng bổ sung thông tin Địa chỉ cư trú để định vị chi nhánh phục vụ.")
    else:
        try:
            Tong_No_Phai_Tra = PTMM + PTMC
            tong_chi_phi_sinh_hoat = 5.0 + (SNPT * 3.5)
            thu_nhap_rong = TN - tong_chi_phi_sinh_hoat
            DTI = Tong_No_Phai_Tra / TN if TN > 0 else 1.0
            LTV = STV / GTTSDB if GTTSDB > 0 else 0.0
            Tich_Luy_Con_Lai = thu_nhap_rong - PTMM

            # Khối kết quả đồng bộ kiến trúc ngân hàng số
            st.markdown('<div class="banking-card">', unsafe_allow_html=True)
            
            tab1, tab2, tab3 = st.tabs(["📈 Phán quyết sơ bộ hệ thống", "📋 Phân tích định lượng dòng tiền", "💡 Giải pháp cấu trúc lại khoản vay"])
            
            with tab1:
                st.write(f"### Khách hàng đăng ký: **{ho_ten.upper()}**")
                m1, m2, m3 = st.columns(3)
                m1.metric(label="Tỷ lệ nợ trên thu nhập (DTI)", value=f"{DTI * 100:.2f}%", delta="Ngưỡng chuẩn: ≤ 70%")
                if "Không cần tài sản" in loai_vay:
                    m2.metric(label="Tỷ lệ Tài sản bảo đảm (LTV)", value="Tín chấp", delta="Không yêu cầu TS")
                else:
                    m2.metric(label="Tỷ lệ Tài sản bảo đảm (LTV)", value=f"{LTV * 100:.2f}%", delta="Ngưỡng chuẩn: ≤ 70%")
                m3.metric(label="Tuổi điều kiện", value=f"{STKH} tuổi", delta="Giới hạn: 18 - 70 tuổi")
                
                st.markdown("---")
                
                rejection_reasons = []
                if CIC == "Nhóm 3 đến 5 - Nợ xấu":
                    rejection_reasons.append("Phát hiện lịch sử nợ quá hạn từ nhóm 3 trở lên (Nợ xấu có nguy cơ mất vốn) tại hệ thống CIC.")
                if CIC == "Nhóm 2 - Nợ cần chú ý" and ("Lý do chủ quan" in ly_do_chuyen_doi or "Lý do cố ý" in ly_do_chuyen_doi):
                    rejection_reasons.append("Lịch sử nợ nhóm 2 đến từ các yếu tố rủi ro phi kỹ thuật.")
                if DTI > 0.70:
                    rejection_reasons.append(f"Chỉ số nợ DTI ở mức quá cao ({DTI * 100:.2f}%), rủi ro vỡ nợ bong bóng do kiệt quệ tài chính.")
                if Tich_Luy_Con_Lai < 0:
                    rejection_reasons.append("Thặng dư tích lũy khả dụng sau khi trừ chi phí sinh hoạt thiết yếu bị âm.")

                if len(rejection_reasons) == 0:
                    st.success("🎉 **HỒ SƠ ĐỦ ĐIỀU KIỆN SƠ TUYỂN (APPROVED)**")
                    st.balloons()
                    st.markdown(f"Hồ sơ của quý khách đạt điểm tín dụng an toàn của hệ thống. Chuyên viên sẽ liên hệ điều phối thu thập hồ sơ giấy tại **{dia_chi}**.")
                else:
                    st.error("🚨 **TỪ CHỐI DUYỆT TỰ ĐỘNG (REJECTED)**")
                    st.markdown("**Danh sách các điều kiện vi phạm chính sách rủi ro ngân hàng:**")
                    for reason in rejection_reasons:
                        st.markdown(f"- *{reason}*")
                        
            with tab2:
                st.write("### Minh bạch cấu trúc dòng tiền hằng tháng:")
                st.write(f"- 💵 **Nghĩa vụ cho khoản vay mới này:** `{PTMM:.2f}` Triệu đồng/tháng")
                st.write(f"- 💳 **Nghĩa vụ nợ cũ tại các đơn vị khác:** `{PTMC:.2f}` Triệu đồng/tháng")
                st.write(f"- 💸 **Hạn mức sinh hoạt cơ bản phân bổ:** `{tong_chi_phi_sinh_hoat:.2f}` Triệu đồng/tháng")
                st.write(f"- 📈 **Thặng dư an toàn còn lại tích lũy:** `{Tich_Luy_Con_Lai:.2f}` Triệu đồng/tháng")

            with tab3:
                st.write("### Khuyến nghị từ Hội đồng thẩm định rủi ro:")
                if DTI > 0.50 and DTI <= 0.70:
                    st.warning("⚠️ Đòn bẩy nợ đang chạm ngưỡng nguy hiểm. Khuyến nghị gia tăng thời gian vay lên tối đa nhằm kéo giãn dòng tiền phải trả mỗi kỳ.")
                if hon_nhan == "Đã kết hôn" and nguon_phu == "Không có":
                    st.info("ℹ️ Khuyên dùng: Nên bổ sung Vợ/Chồng vào vai trò người đồng vay để tăng năng lực chứng minh dòng tiền.")
                if len(rejection_reasons) == 0 and so_lan_tra_cham == 0:
                    st.write("✅ Khách hàng có điểm uy tín tài chính xuất sắc. Đề xuất áp dụng gói lãi suất ưu đãi ưu tiên.")
            
            st.markdown('</div>', unsafe_allow_html=True)
                                    
        except ZeroDivisionError:
            st.error("❌ Có lỗi xảy ra trong quá trình xử lý toán học dữ liệu.")
