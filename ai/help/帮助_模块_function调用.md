# 帮助:模块/function调用

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E6%A8%A1%E5%9D%97/function%E8%B0%83%E7%94%A8
revid：33329 · 抓取时间：2026-11-09T14:27:10+08:00

---

{{LuaNav}}
编程的一个常见模式是将不同的功能模块化为不同的[[帮助:模块/函数|function]]，并在function之间互相调用（“通信”，即传递参数，返回结果）。上述例子并未涉及到这一层面，下面我们来介绍如何在同一个模块中，为两个不同的function进行协作。
'''例[1]'''
<pre>
local p = {}
function p.print_text(frame)         -------函数A
local args = frame.args                  -------------引用frame.args以获取模板传进来的参数
  local text =  p.text_render(args[1],args[2],args[3])          ----------将函数A中的参数传入函数B
return text
end

function p.text_render(name,level,type)      --------函数B
local res = name..'是一件'.. lavel ..'级的' .. type .. '。'             ---------拼接字符串
  return res                     ----------返回拼接完成的结果（对于本例子而言，仅有函数A调用了函数B，因此函数A获取了函数B的运算结果）
end
return p
</pre>

我们可以看到，在上一节的例子上，我们又添加了一个专门处理字符拼接的function——“text_render”，在text_render名字后面的括号中，<code>name</code>,<code>level</code>,<code>type</code>是该function中所使用的参数。我们将例[1]中print_text的三个外部参数args[1],args[2],args[3]，通过下列语法传递给text_render
<pre>
p.text_render(args[1],args[2],args[3])
</pre>
对应的，在function“text_render”中，args[1] -->name，args[2] -->level，args[3] -->type
<pre>
p.text_render(name,level,type)
</pre>
在function“.text_render”中将三个参数处理完成后，拼接成字符串“res”，再通过return返回给“print_text”，输出给MediaWiki。就这样，我们完成了一次完整的function之间的参数传递和调用。事实上，更复杂的lua模块依然是按照这一模式进行工作。
