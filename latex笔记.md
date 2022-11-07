先做个笔记，要用到的时候再学 :)



在线表格转latex格式 https://tablesgenerator.com/

在线公式转latex格式 https://latex.91maths.com/ 

识别手绘数学符号，展示对应的符号及其latex代码 https://detexify.kirelabs.org/classify.html

---

搬运自博客 https://blog.csdn.net/qq_21891843/article/details/121380757

文件开始的预备工作：

```latex
%\documentclass{cumcmthesis}
\documentclass[withoutpreface,bwprint]{cumcmthesis} %去掉封面与编号页，电子版提交的时候使用。

\usepackage{xeCJK}
\usepackage[framemethod=TikZ]{mdframed}
\usepackage{url}   % 网页链接
\usepackage{subcaption} % 子标题

\usepackage{float}%图片[H]
\usepackage{listings} %插入代码
\usepackage{xcolor} %代码高亮

\lstset{numbers=left, %设置行号位置
	numberstyle=\tiny, %设置行号大小
	keywordstyle=\color{blue}, %设置关键字颜色
	commentstyle=\color[cmyk]{1,0,1,0}, %设置注释颜色
	frame=single, %设置边框格式
	escapeinside=`, %逃逸字符(1左面的键)，用于显示中文
	%breaklines, %自动折行
	extendedchars=false, %解决代码跨页时，章节标题，页眉等汉字不显示的问题
	xleftmargin=2em,xrightmargin=2em, aboveskip=1em, %设置边距
	tabsize=4, %设置tab空格数
	showspaces=false %不显示空格
}
```



## 1、标题以及摘要

```latex
\title{一篇简短的Latex教程}
\begin{document}
	\maketitle    
	\begin{abstract}
		这是一段摘要。
		\keywords{摘要\quad  教程}
	\end{abstract}     
\end{document}
```



##  2、目录、段落

 ```latex
\begin{document}
%生成目录设置
\tableofcontents

\newpage
%标题开始
\section{一级标题1}
这一段是一级标题1下的内容\par
这一段是一级标题1下的内容
\subsection{二级标题}
这一段是二级标题下的内容
\subsubsection{三级标题下的内容}
这一段是三级标题下的内容
\section{一级标题2}
这一段是一级标题2下的内容
\end{document}
 ```
 

## 3、插入图片

首先要在目录下创建一个文件夹

```latex
\begin{document}
 \setcounter{figure}{0}  %将图序号清零
 \begin{figure}[H]
	\centering
	\includegraphics[width=.6\textwidth]{蛇的移动} %这是图片文件名字
	\caption{蛇的移动} %这是底下文字
	\label{1-1}
 \end{figure}
 \begin{figure}
	\centering
	\begin{minipage}[c]{0.48\textwidth}
		\centering
		\includegraphics[height=0.2\textheight]{f1}
		\subcaption{图1}
	\end{minipage}
	\begin{minipage}[c]{0.48\textwidth}
		\centering
		\includegraphics[height=0.2\textheight]{f1}
		\subcaption{图2}
	\end{minipage}
	\caption{多图并排示例}
 \end{figure}
\end{document}
```



## 4、表格以及三线表

表格：

```latex
\begin{document}
  \begin{tabular}{|l|c|r|}
	\hline
	操作系统& 发行版& 编辑器\\
	\hline
	Windows & MikTeX & TexMakerX \\
	\hline
	Unix/Linux & teTeX & Kile \\
	\hline
	Mac OS & MacTeX & TeXShop \\
	\hline
	通用& TeX Live & TeXworks \\
	\hline
\end{tabular}
\end{document}
```

三线表：
```latex
\begin{table}[!htbp]
	\caption{符号说明}\label{tab:001} \centering
	\begin{tabular}{cc}
		\toprule[1.5pt]
		符号 & 说明\\
		\midrule[1pt]
		$r_{k}(x)$			&为选定的线性无关函数\\
		$\partial_{k}$		&为待定系数\\
		$k_{0}$				&潜在力度\\
		$g(t)$				&政府力度\\
		$\beta$				&患病潜伏期的转化率\\
		$\mu$				&病死率\\
		$\partial$			&权重\\
		$R_{t}$				&治愈人数\\
		$I_{t}$				&每日病例数\\
		\bottomrule[1.5pt]
	\end{tabular}
\end{table}
\end{document}
```



## 5、行内小矩阵

 ```latex
\title{一篇简短的Latex教程}
\begin{document}
 这是一个行内小矩阵$ ( \begin{smallmatrix} a&b\\c&d \end{smallmatrix} ) $。
\end{document}
 ```



## 6、有序列表与无序列表

```latex
\begin{document}
	\begin{enumerate} %有序列表
		\item one
		\item two
		\item ...
	\end{enumerate}

	\begin{itemize} %无序列表
		\item one
		\item two
		\item ...
	\end{itemize}
\end{document}
```



## 7、居中显示、脚注、加粗、斜体

注意！斜体只能斜英文！！

```latex
\begin{document}
 \centerline{居中显示}
 未加粗字体，\textbf{加粗字体}\par
 \textit{Beautiful\footnote{1}}
\end{document}
```



##  8、参考文献、引用

 ```latex
\begin{document}
	引用参考文献\cite{1}.
	\begin{thebibliography}{9}%宽度9
		\bibitem[1]{1} %{1}为此参考文献标记
		（美）Frank R.Giordano Maurice D.Weir William P.Fox 著叶其孝姜启源等译.数学建模[M].机械工业出版社.2019.10
		\bibitem[2]{2}
		司守奎，孙兆亮.数学建模算法与应用[M].北京：国防工业出版社.2015.4
		\bibitem[3]{3}
		盛骤，谢式千，潘承毅.概率论与数理统计[M].4 版.北京：高等教育出版社.2010：254-259.
		\bibitem[4]{4}
		宋倩倩,赵涵,方立群,等.新型冠状病毒肺炎的早期传染病流行病学参数估计研究[J].中华流行病学杂志，2020，41（4）
		\url {https://www.who.int/emergencies/diseases/novel-coronavirus-2019/events-as-they-happen.}
	\end{thebibliography}
\end{document}
 ```



##  9、表格代码

 ```latex
\begin{document}
	\begin{tcode}
		\begin{table}[!htbp]
			\caption[标签名]{中文标题}
			\begin{tabular}{cc...c}
				\toprule[1.5pt]
				表头第1个格   & 表头第2个格   & ... & 表头第n个格  \\
				\midrule[1pt]
				表中数据(1,1) & 表中数据(1,2) & ... & 表中数据(1,n)\\
				表中数据(2,1) & 表中数据(2,2) & ... & 表中数据(2,n)\\
				...................................................\\
				表中数据(m,1) & 表中数据(m,2) & ... & 表中数据(m,n)\\
				\bottomrule[1.5pt]
			\end{tabular}
		\end{table}
	\end{tcode}
\end{document}

 ```



##  10、各类公式以及定理定引理推论等

 ```latex
\begin{document}
首先是行内公式，例如 $ \theta $ 是角度。行内公式使用 \verb|$  $| 包裹。

行间公式不需要编号的可以使用 \verb|\[  \]| 包裹，例如
\[
E=mc^2
\]
其中 $ E $ 是能量，$ m $ 是质量，$ c $ 是光速。

如果希望某个公式带编号，并且在后文中引用可以参考下面的写法：
\begin{equation}
	E=mc^2
	\label{eq:energy}
\end{equation}
式\cref{eq:energy}是质能方程。

多行公式有时候希望能够在特定的位置对齐，以下是其中一种处理方法。
\begin{align}
	P & = UI \\
	& = I^2R
\end{align}
\verb|&| 是对齐的位置， \verb|&| 可以有多个，但是每行的个数要相同。

矩阵的输入也不难。
\[
\mathbf{X} = \left(
\begin{array}{cccc}
	x_{11} & x_{12} & \ldots & x_{1n}\\
	x_{21} & x_{22} & \ldots & x_{2n}\\
	\vdots & \vdots & \ddots & \vdots\\
	x_{n1} & x_{n2} & \ldots & x_{nn}\\
\end{array} \right)
\]

分段函数这些可以用 \verb|case| 环境，但是它要放在数学环境里面。
\[
f(x) =
\begin{cases}
	0 &  x \text{为无理数} ,\\
	1 &  x \text{为有理数} .
\end{cases}
\]
在数学环境里面，字体用的是数学字体，一般与正文字体不同。假如要公式里面有个别文字，则需要把这部分放在 \verb|text| 环境里面，即 \verb|\text{文本环境}| 。

公式中个别需要加粗的字母可以用 \verb|$\bm{math symbol}$| 。如 $ \alpha a\bm{\alpha a} $ 。

以上仅简单介绍了基础的使用，对于更复杂的需求，可以阅读相关的宏包手册，如 \href{http://texdoc.net/texmf-dist/doc/latex/amsmath/amsldoc.pdf}{amsmath}。

希腊字母这些如果不熟悉，可以去查找符号文件 \href{http://mirrors.ctan.org/info/symbols/comprehensive/symbols-a4.pdf}{symbols-a4.pdf} ，也可以去 \href{http://detexify.kirelabs.org/classify.html}{detexify} 网站手写识别。另外还有数学公式识别软件 \href{https://mathpix.com/}{mathpix} 。

下面简单介绍一下定理、证明等环境的使用。
\begin{definition}
	定义环境
	\label{def:nosense}
\end{definition}
\cref{def:nosense}除了告诉你怎么使用这个环境以外，没有什么其它的意义。

除了 definition 环境，还可以使用 theorem 、lemma、corollary、assumption、conjecture、axiom、principle、problem、example、proof、solution 这些环境，根据论文的实际需求合理使用。

\begin{theorem}
	这是一个定理。
	\label{thm:example}
\end{theorem}
由\cref{thm:example}我们知道了定理环境的使用。

\begin{lemma}
	这是一个引理。
	\label{lem:example}
\end{lemma}
由\cref{lem:example}我们知道了引理环境的使用。

\begin{corollary}
	这是一个推论。
	\label{cor:example}
\end{corollary}
由\cref{cor:example}我们知道了推论环境的使用。

\begin{assumption}
	这是一个假设。
	\label{asu:example}
\end{assumption}
由\cref{asu:example}我们知道了假设环境的使用。

\begin{conjecture}
	这是一个猜想。
	\label{con:example}
\end{conjecture}
由\cref{con:example}我们知道了猜想环境的使用。

\begin{axiom}
	这是一个公理。
	\label{axi:example}
\end{axiom}
由\cref{axi:example}我们知道了公理环境的使用。

\begin{principle}
	这是一个定律。
	\label{pri:example}
\end{principle}
由\cref{pri:example}我们知道了定律环境的使用。

\begin{problem}
	这是一个问题。
	\label{pro:example}
\end{problem}
由\cref{pro:example}我们知道了问题环境的使用。

\begin{example}
	这是一个例子。
	\label{exa:example}
\end{example}
由\cref{exa:example}我们知道了例子环境的使用。

\begin{proof}
	这是一个证明。
	\label{prf:example}
\end{proof}
由\cref{prf:example}我们知道了证明环境的使用。

\begin{solution}
	这是一个解。
	\label{sol:example}
\end{solution}
由\cref{sol:example}我们知道了解环境的使用。
\end{document}
 ```