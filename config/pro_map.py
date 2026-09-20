# 属性词条后缀 → 中文名 映射表
#
# 用于补全 medelPropertyClass 中带后缀的属性名（如 dpsMul_rifle）。
# 这些后缀词条由 AS 代码后期拼接生成，原 XML 中不存在中文名。
# 补全规则：基础词条中文名 + "/" + 后缀中文名
#   例：dpsMul（战斗力）+ rifle（火炮）→ dpsMul_rifle = 战斗力/火炮
#
# 后缀通常对应武器类型（armsType）。

SUFFIX_MAP = {
    "rifle": "步枪",
    "sniper": "狙击枪",
    "shotgun": "散弹枪",
    "pistol": "手枪",
    "rocket": "火炮",
    "flamer": "喷火器",
}
