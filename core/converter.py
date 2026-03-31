from typing import Any

class ValueConverter:
    '''
    智能数值转换器。
    用于将 XML 中的字符串属性转换为 Python 原生类型（int, float, bool, list）。
    爆枪的游戏数据命名遵循一定规范（如 B 结尾为布尔，Arr 结尾为数组），本类据此进行自动化处理。
    '''
    
    @staticmethod
    def to_smart_value(value: str, key_name: str = "") -> Any:
        '''
        根据键名和值内容，智能推断并转换数据类型。
        
        参数:
            value: XML 节点中的原始字符串值。
            key_name: 字段名称，用于辅助判断类型（如是否为布尔或数组）。
        
        逻辑:
            1. 处理布尔值：字段名以 'B' 结尾，且值为 'true' 或 '1'。
            2. 处理数组：字段名以 'Arr' 结尾或内容包含逗号。哪怕只有单个元素也会转化为 list。
            3. 处理十六进制：保留 0x 开头的字符串（通常为颜色值）。
            4. 处理数字：尝试转换为 int 或 float。
            5. 保底处理：返回原始去空格字符串。
        '''
        if value is None: return None
        value = value.strip()
        if not value: return ""

        # 布尔逻辑判断：判断键名是否以 B 结尾（如 isCoolB）
        if key_name and key_name.endswith('B'):
            val_lower = value.lower()
            return val_lower in ('true', '1')

        # 数组逻辑判断：判断键名是否以 Arr 结尾（如 skillArr）或包含逗号
        if (key_name and key_name.endswith('Arr')) or ',' in value:
            # 分割字符串并去除空项
            parts = [v.strip() for v in value.split(',') if v.strip()]
            return [ValueConverter._cast_single_value(p) for p in parts]

        # 十六进制处理：主要针对颜色值 (如 0xffffff)
        if value.startswith('0x'):
            return value

        # 常规类型转换
        return ValueConverter._cast_single_value(value)

    @staticmethod
    def _cast_single_value(v: str) -> Any:
        '''内部私有方法：处理单一值的数字/字符串转换。'''
        try:
            if '.' in v:
                return float(v)
            return int(v)
        except (ValueError, TypeError):
            return v