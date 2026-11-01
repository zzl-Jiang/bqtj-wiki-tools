# XML 文件屏蔽列表
#
# 这些文件不属于游戏正式数据（多为调试/测试/活动残留），
# 提取时应全部跳过。
#
# 注意：只记录文件名中的关键片段，不含 "数字前缀" 和 "Class" 后缀，
#      因为这些会随版本更新变动。
#      例如 xml/294_XMLOut_file_xinLingP1Class.bin 只需记录 "file_xinLingP1"。

SKIP_XML_KEYWORDS = (
    "file_xinLingP1",
    "file01_lie",
    "file02_zhan",
    "file03_bu",
    "file_qianyouNiubi19",
    "file_qianyouNiubi2025debug",
)


def is_skipped_xml(filename: str) -> bool:
    """判断 XML 文件名是否在屏蔽列表中"""
    if not filename:
        return False
    return any(keyword in filename for keyword in SKIP_XML_KEYWORDS)
