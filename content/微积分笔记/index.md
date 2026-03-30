---
title: "微积分笔记"
date: 2026-03-30
---

### 初等数学基础

#### 三角函数恒等变换

- **平方关系**
$$
sin^2\theta + cos^2\theta = 1, \quad 1 + tan^2\theta = sec^2\theta, \quad 1 + cot^2\theta = csc^2\theta
$$
- **诱导公式**
$$\left\{
\begin{array}{ll}
\text{(1) } sin\left(\dfrac{\pi}{2} \pm \alpha\right) = cos\alpha  &  \\
\text{(2) } sin (\pi \pm \alpha) = \mp sin\alpha & \\
\text{(3) } cos\left(\dfrac{\pi}{2} \pm \alpha\right) = \mp sin\alpha &  \\
\text{(4) } cos (\pi \pm \alpha) = -cos\alpha &
\end{array}
\right.$$

   > **奇变偶不变，符号看象限**  
   > - $\frac{\pi}{2}$的奇数倍 → 函数名改变（sin↔cos）  
   > - $\frac{\pi}{2}$的偶数倍 → 函数名不变  
   > - 符号由$\alpha$视为锐角时原函数在对应象限的符号决定

- **和差角**
$$
\begin{align*}
sin(\alpha \pm \beta) &= sin\alpha cos\beta \pm cos\alpha sin\beta \\ncos(\alpha \pm \beta) &= cos\alpha cos\beta \mp sin\alpha sin\beta \\ntan(\alpha \pm \beta) &= \frac{tan\alpha \pm tan\beta}{1 \mp tan\alpha tan\beta}
\end{align*}
$$

- **倍角公式**
$$
\begin{align*}
sin 2\theta &= 2 sin\theta cos\theta \\ncos 2\theta &= 1 - 2 sin^2\theta \\ntan 2\theta &= \frac{2 tan\theta}{1 - tan^2\theta}
\end{align*}
$$

- **半角公式**
$$
\begin{align*}
sin \frac{\theta}{2} &= \pm \sqrt{\frac{1 - cos\theta}{2}} \\ncos \frac{\theta}{2} &= \pm \sqrt{\frac{1 + cos\theta}{2}} \\ntan \frac{\theta}{2} &= \pm \sqrt{\frac{1 - cos\theta}{1 + cos\theta}} 
= \frac{sin\theta}{1 + cos\theta} 
= \frac{1 - cos\theta}{sin\theta}
\end{align*}
$$

- **降幂公式**
$$
\begin{align*}
sin^2\theta &= \frac{1 - cos 2\theta}{2} \\ncos^2\theta &= \frac{1 + cos 2\theta}{2} \\ntan^2\theta &= \frac{1 - cos 2\theta}{1 + cos 2\theta}
\end{align*}
$$
- **和差化积**
$$
\begin{align*}
sin\alpha + sin\beta &= 2 sin\frac{\alpha+\beta}{2} cos\frac{\alpha-\beta}{2} \\nsin\alpha - sin\beta &= 2 cos\frac{\alpha+\beta}{2} sin\frac{\alpha-\beta}{2} \\ncos\alpha + cos\beta &= 2 cos\frac{\alpha+\beta}{2} cos\frac{\alpha-\beta}{2} \\ncos\alpha - cos\beta &= -2 sin\frac{\alpha+\beta}{2} sin\frac{\alpha-\beta}{2}
\end{align*}
$$

- **积化和差**
$$
\begin{align*}
sin\alpha cos\beta &= \frac{1}{2} [sin(\alpha+\beta) + sin(\alpha-\beta)] \\ncos\alpha sin\beta &= \frac{1}{2} [sin(\alpha+\beta) - sin(\alpha-\beta)] \\ncos\alpha cos\beta &= \frac{1}{2} [cos(\alpha+\beta) + cos(\alpha-\beta)] \\nsin\alpha sin\beta &= -\frac{1}{2} [cos(\alpha+\beta) - cos(\alpha-\beta)]
\end{align*}
$$

- **万能代换**
	令 $t = tan\frac{\theta}{2}$：
$$
sin\theta = \frac{2t}{1+t^2}, \quad cos\theta = \frac{1-t^2}{1+t^2}, \quad tan\theta = \frac{2t}{1-t^2}
$$

- **辅助角**
$$
\begin{align*}
a sin\theta + b cos\theta &= \sqrt{a^2+b^2} sin(\theta + \varphi) \\ntan\varphi &= \frac{b}{a} \quad (\text{相位角})
\end{align*}
$$

---

#### 多项式因式分解
**常用方法：**
- 提取公因式
- 十字相乘法（二次三项式）
- 分组分解法
- 公式法（平方差、立方和、立方差等）
- 因式定理：若 $P(r)=0$，则 $(x-r)$ 是因式
- 综合除法（高阶多项式）

**常用公式：**
$$
\begin{aligned}
\begin{align*}
a^2 - b^2 &= (a - b)(a + b) \\na^3 + b^3 &= (a + b)(a^2 - ab + b^2) \\na^3 - b^3 &= (a - b)(a^2 + ab + b^2) \\n(a + b)^2 &= a^2 + 2ab + b^2 \\n(a - b)^2 &= a^2 - 2ab + b^2 \\n(a + b)^3 &= a^3 + 3a^2b + 3ab^2 + b^3 \\n(a - b)^3 &= a^3 - 3a^2b + 3ab^2 - b^3 \\na^n - b^n &= (a - b)(a^{n-1} + a^{n-2}b + \cdots + ab^{n-2} + b^{n-1}) \\na^n + b^n &= (a + b)(a^{n-1} - a^{n-2}b + \cdots - ab^{n-2} + b^{n-1}) \quad (n\text{为奇数}) \\n(a + b)^n &= \sum_{k=0}^{n} \binom{n}{k} a^{n - k}b^k \quad \text{(二项式定理)}
\end{align*}
\end{aligned}
$$

#### 常见体积表面积

| 几何体 | 表面积 \(S\)                                       | 体积 \(V\)                                          |
| --- | ----------------------------------------------- | ------------------------------------------------- |
| 圆锥  | $S = \pi r l$                                   | $V = \frac{1}{3} \pi r^2 h$                       |
| 圆台  | $S = \pi (r_1 + r_2) l + \pi r_1^2 + \pi r_2^2$ | $V = \frac{1}{3} \pi h (r_1^2 + r_2^2 + r_1 r_2)$ |
| 球   | $S = 4\pi R^2$                                  | $V = \frac{4}{3} \pi R^3$                         |

---

### 极限与微分

#### 极限相关

##### 数列极限类特例

找特例时注意——数列可以是跳变的，在不同子序列上行为不同！**比如奇偶项规律完全不一样**

**相乘无限 必有一无限 是错的**

$$a_{n}=\cases{n^{2},n为奇数\\  \dfrac{1}{n},n为偶数}  \quad b_{n}=\cases{\dfrac{1}{n},n为奇数\\  n^{2},n为偶数}$$

##### 求极限方法
$$
\lim_{x \to 0} \frac{sin x}{x} = 1, \quad  
\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e \quad
\lim_{x \to \infty} x^{1/x} = 1
$$
- 泰勒展开非常有效，有效规避各种所谓的恒等变形。但是注意展开的次数要足够。
	- **先通分再展开**，避免分母提前展开后通分损失有用的高阶项
- 洛必达（要求在$x_{0}$**去心邻域内**可导）
- $f(x)-f(x+\delta x)$差值极限，用拉格朗日中值定理。常见：对数、三角函数的差值

- 转化为定积分$$\lim_{n \rightarrow \infty} \sum^{n}_{i=1} \frac{1}{n}f(\frac{i}{n})=\int^{1}_{0} f(x)dx$$
	- 本质上是分成无穷多份，每一份用一个点的函数值，可以取区间上任何一个点$$\lim_{n \to \infty} \frac{b-a}{n} \sum_{k=1}^n f\left(a + \frac{k(b-a)}{n}\right) = \int_a^b f(x) dx$$
	- 但是我更喜欢，这样不用凑常数：$$
\lim_{n \to \infty} \sum_{i=1}^{n} g\left(\frac{b - a}{n}i\right) \frac{b-a}{n} = \int_{0}^{b-a} g(t) \mathrm{d}t.
$$
- 识别多重积分
	- 若 $\sum_{i=1}^{n} \sum_{j=1}^{n}$ → 区域是正方形 $0 \leq x \leq 1, 0 \leq y \leq 1$
	- 若 $\sum_{i=1}^{n} \sum_{j=1}^{i}$ → 区域是三角形 $0 \leq x \leq 1, 0 \leq y \leq x$（或交换 $x, y$ ，取决于谁做外求和）。


一些代数变形的技巧：
- 差值转化为比值（找**公因式**），尤其是趋于无穷的时候
 $$
e - \left(1 + \frac{1}{x}\right)^x = e - e^{x \ln \left(1 + \frac{1}{x}\right)} = e \left[1 - e^{x \ln \left(1 + \frac{1}{x}\right) - 1}\right].
$$
$$\ln(a+x)=\ln x +\ln(1+\frac{a}{x})，差值可估计$$

##### 证明数列极限

在考研数学，几乎只使用
- 单调有界
- 证明数列求和的级数收敛，从而得到数列收敛

压缩映射：
- 若 $x_{n+1} = f(x_n), a = f(a), |f'(x)| \leq k < 1$，则可以直接证明收敛到不动点。考虑$$|x_{n+1} - a| = |f(x_n) - f(a)| = |f'(\xi)| |x_n - a| \leq k |x_n - a| \leq k^2 |x_{n-1} - a| \leq \cdots \leq k^n |x_1 - a|,$$
- 变式：$|f'(x)| \leq kf(x), k < 1$，$x_{n+1}=\ln (f(x_{n}))$，一样的道理

##### 保号性与有界性

保号：
1.  若 $\lim_{x \to x_0} f(x) = A > 0$（或 $A < 0$)，则存在 $\delta > 0$，使得当 $0 < |x - x_0| < \delta$ 时，有 $f(x) > 0$（或 $f(x) < 0$）。
2.  若存在 $\delta > 0$，使得当 $0 < |x - x_0| < \delta$ 时 $f(x) \geq 0$（或 $f(x) \leq 0$)，且 $\lim_{x \to x_0} f(x) = A$，则 $A \geq 0$（或 $A \leq 0$)。
3.  常用于证明题取点，如$f(0)=a,f'(0)>0（这是一个极限式子） \implies \exists \zeta, f(\zeta)>a, \zeta \in (0, \delta)$，这里不能推知$f'$是因为不一定连续
4. 如果告知了$f$**连续**，则$\lim f(x_{0})>0 \implies \exists \zeta, f(\zeta)>0, \zeta \in (0, \delta)$


有界：
- 若 $\lim_{x \to x_0} f(x) = A$，则存在常数 $M > 0$ 和 $\delta > 0$，使得当 $0 < |x - x_0| < \delta$ 时，有 $|f(x)| \leq M$
- 常用于放缩，比如$x$充分大时，$f(x)>\frac{M}{2}$

#### 连续、可积、有界

##### 间断点求解

- 找到函数无意义的点：分母为0、函数本身无定义（$\tan \pi/2$）
- 然后求这些点的左右极限，看左连续、右连续情况
	- 左极限 $=$ 右极限 $\ne f(x_0)$ 或 $f(x_0)$ 无定义，可去间断点
	- 左极限不等于右极限，但都存在，跳跃
	- 至少一个不存在，趋于 $\infty$ 或振荡

##### 连续与可积

- 由弱到强：
	- 可积、连续、在$x_{0}$点可导、在邻域上可导、连续可导（导函数连续）、
	- 在$x_{0}$点二阶可导、在邻域上二阶可导……
- 可积的判定
	1. 闭区间上的连续函数必可积
	2. 只有有限个间断点的有界函数可积
	3. 单调有界函数可积
- 注意在某点有导数值，严格弱于，导函数连续
- 变上限函数的连续性：$\int^{x}_{0} f(x)$，若$f$可积，则连续；若$f$连续，则可导

“可积”与“是某个函数的导函数”之间**没有必然的包含关系**，并且**两者都弱于连续**

##### 有界

- **断点**或趋于**无穷**，可能无界
- 进而可以得到
	- 闭区间连续，必有界（无断点、无无穷）
	- 开区间连续，端点极限存在，必有界（断点处有界）
	- 有限长开区间导函数有界（积分值有界）

$f$与$f^{'}$的极限、有界性
- $f$ 极限存在 是 $f^{'}$ 极限存在的 **既不充分也不必要条件**（举例：$\frac{1}{x} sin x^2$、$\ln x$）
- $f$ 有界 是$f^{'}$ 有界的 **既不充分也不必要**条件（举例：$sin x^{2}$，导数为$2x cos x^{2}$可以无穷大）
	- 导函数趋于 0（有界且极限存在） 不能保证函数有界
- **导函数极限存在而非零**则表明类似存在渐近线，近似线性增长
- 记住反例：振荡衰减、对数增长、线性函数

##### 周期

$f$与$f^{'}$的周期性、奇偶性
- 导函数是周期函数，原函数不一定也是周期函数；原函数是周期函数，导函数一定也是
- 原函数是可导的奇（偶）函数 ⇒ 导函数是偶（奇）函数
- 导函数是偶函数 ⇒ 原函数不一定是奇函数，可能具有常数项！
- 导函数是奇函数 ⇒ 原函数一定是偶函数

#### 求导

##### 定义

- $f'(x_0) = \lim_{\Delta x \to 0} \dfrac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$
- $f'(0) = \lim_{n\to \infty} n[f(\frac{1}{n}) - f(0)]$
- 可导，对称差商极限存在$L = \lim_{\Delta x \to 0} \dfrac{f(a + \Delta x) - f(a - \Delta x)}{2 \Delta x}$
- 对称差商极限存在，不一定能推出可导。比如$$
f(x) = 
\begin{cases} 
x^2, & x \geq 0, \\n-x, & x < 0,
\end{cases}
\quad a = 0
$$
- 如果二阶可微，二阶导数可以直接写作（对h求导一次）：
 $$\begin{align}
\lim_{h \to 0} \frac{f(x+h) + f(x-h) - 2f(x)}{h^2} &= \lim_{h \to 0} \frac{f'(x+h) - f'(x-h)}{2h}\\
&= \lim_{h \to 0} \frac{1}{2} \left[ \frac{f'(x+h) - f'(x)}{h} + \frac{f'(x-h) - f'(x)}{-h} \right] = f''(x).
\end{align}$$

##### 计算

很熟悉的
$$
\begin{aligned} \frac{d}{dx}(c) &= 0 \\ \frac{d}{dx}(x^n) &= nx^{n-1} \\ \frac{d}{dx}(e^x) &= e^x \\ \frac{d}{dx}(a^x) &= a^x\ln a \\ \frac{d}{dx}(\ln x) &= \frac{1}{x} \\ \frac{d}{dx}(\log_a x) &= \frac{1}{x\ln a} \\&= \\ \frac{d}{dx}(sin x) &= cos x \\ \frac{d}{dx}(cos x) &= -sin x \\  \end{aligned}
$$

不是那么熟悉的：
$$\begin{aligned}  \frac{d}{dx}(tan x) &= sec^2 x \\ \frac{d}{dx}(cot x) &= -csc^2 x \\ \frac{d}{dx}(sec x) &= sec x tan x \\ \frac{d}{dx}(csc x) &= -csc x cot x \\&= \\ \frac{d}{dx}(arcsin x) &= \frac{1}{\sqrt{1-x^2}} \\ \frac{d}{dx}(arccos x) &= -\frac{1}{\sqrt{1-x^2}} \\ \frac{d}{dx}(arctan x) &= \frac{1}{1+x^2} \end{aligned}$$

莱布尼茨高阶导：$$(uv)^{(n)} = \sum^{n}_{k=0} u^{(n-k)} v^{(k)}$$

#### 基本泰勒展开

两种形式
- 带皮亚诺余项，不估计高阶无穷小
- 带拉格朗日余项，给出高阶无穷小的估计值：$R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x-x_0)^{n+1} \ (\xi \text{ 在 } x_0,x\text{ 之间})$。

常用的
$$
\begin{aligned}
e^x &= \sum \frac{x^n}{n!} + R_n(x) \\
sin x &= \sum (-1)^k \frac{x^{2k+1}}{(2k+1)!} + R_{2k+1}(x) \\
cos x &= \sum (-1)^k \frac{x^{2k}}{(2k)!} + R_{2k}(x) \\
\ln(1+x) &= \sum (-1)^{n-1} \frac{x^n}{n} + R_n(x) \\
(1+x)^\alpha &= \sum \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!} x^k + R_n(x) \\
arctan x &= \sum (-1)^k \frac{x^{2k+1}}{2k+1} + R_{2k+1}(x) \\
\end{aligned}
$$

不太常用也记不太住的
$$\begin{aligned}
(1+x)^\alpha &= \sum \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!} x^k + R_n(x) \\
(1+x)^\alpha &= 1+\alpha x  +\dfrac{\alpha (\alpha-1)}{2}x^{2}\\
\\narcsin x &= \sum \frac{(2k-1)!!}{(2k)!!} \frac{x^{2k+1}}{2k+1} + R_{2k+1}(x) \\
arcsin x &= x+\frac{x^{3}}{6}+\frac{3x^{5}}{40}\\
\\ntan x &= \sum_{n=1}^{\infty} \frac{B_{2n}(-4)^n(1-4^n)}{(2n)!} x^{2n-1} + R_{2n}(x)\\ntan x &= x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} + \frac{62x^9}{2835} + \cdots + R_{2n}(x)
\end{aligned}$$

##### 应用

- 利用泰勒展开估计**导数的范数**、函数的局部性质、**积分值**

#### 函数的渐进行为

**函数值与变化率（导数）的渐近行为可以分离**
- 从**导数**信息推**函数**信息，通常更直接、更可行（如命题①，泰勒公式）。
- 从**函数**信息反推**导数**信息，必须格外小心，通常需要附加条件（如导数极限存在、函数高阶可导等）

##### 在某一点

- 如果 $f$在 $a$点 存在 $n$阶导数​ $f^{n} (a)$，则必能写出上述带皮亚诺余项的 $n$阶泰勒公式（即展开式成立）
- 反之，**能写出n阶泰勒公式，不意味着有邻域上的导数，更不意味着存在在该点的n阶导数**
	- 连续函数$f \sim x+ 2x^{2}+\Omega(x)$，不意味着$f$在邻域内有一阶导数（也就不意味着存在高阶导数在某点的值），**只能说明有$f^{'}(0)$在某点**
	- $\lim_{x \to 0} \dfrac{f(x)}{x^n}=0$，未说明$f$可导时，只能推出$f^{'}(0)$存在
	- 例如$f(x)=x+ x^{2} sin \dfrac{1}{x}$

- 对于高阶导数（如 $f''(0)$），**除非题目明确声明函数高阶可导**，否则不能判别

##### 在无穷远

- 如果有导数情况：$\lim_{x \to \infty} f^{'}(x)=a$，可以推导出$f(x) \sim ax$
- 反之不成立！不能错误地将函数渐近行为$f(x)∼ax$直接推广到导数的极限。
- 即使 $f(x)$的整体趋势接近线性函数 $ax$，其局部变化率（导数）可能因振荡而不收敛。（但是如果附加条件f′(x)的极限存在，就可以推出了）


#### 几何

##### 凹凸

- $f^{''}>0$，凹函数（记住$x^{2}$是凹函数）
- 凹凸性的几何特征非常丰富：
	- 切线、函数曲线、割线的关系
	- 函数积分、 切线积分、 割线积分的关系
	- $f(a)+f(b)$可以和梯形面积联系——割线积分
- 一阶泰勒展开（线性部分）加上**二阶导正定**，结合积分产生不等式

##### 渐近线

- 无定义点：可能存在铅锤渐近线
- $\lim_{x \rightarrow \infty} f(x)=a$，则存在水平渐近线
- 斜渐近线分两步：
	- $\lim_{x \rightarrow \infty} \dfrac{f(x)}{x}=k$，说明存在（一阶近似）
	- $\lim_{x \rightarrow \infty} f(x)-kx$，求得截距（渐进）

##### 拐点

拐点是$f^{''}$**变号**的点，不一定要连续！

第三充分条件
- 设 $f''(x_0) = f'''(x_0) = \cdots = f^{(n-1)}(x_0) = 0$，$f^{(n)}(x_0) \neq 0$：
- 若 $n$ 为奇数（$n \geq 3$），则 $x_0$ 是拐点

##### 曲率半径

- 曲线 $y=f(x)$ 在点 $(x,y)$ 处：
$$
\text{曲率 } \kappa = \dfrac{|y''|}{(1+(y')^2)^{\frac{3}{2}}}, \quad  
\text{曲率半径 } \rho = \frac{1}{\kappa}
$$
- 曲率圆$(x-a)^{2}+(y-b)^{2}=r^{2}$，求导可得$y^{'}$、$y^{''}$

![曲率半径](/Notes-for-GradEntranceExam/微积分笔记/assets/微积分公式结论汇总/file-20251220230552656.png)

#### 极值第三充分条件
设 $f^{(k)}(x_0) = 0 \ (k=1,2,\cdots,n-1)$，$f^{(n)}(x_0) \neq 0$：
- 若 $n$ 为偶数：
  - $f^{(n)}(x_0) > 0$ $\Rightarrow$ 极小值点
  - $f^{(n)}(x_0) < 0$ $\Rightarrow$ 极大值点
- 若 $n$ 为奇数：非极值点


#### 中值定理

##### 定理

- **介值定理**：若函数 $f(x)$在闭区间 $[a,b]$上连续，且 $u$是介于 $f(a)$与 $f(b)$之间的任意一个实数（即满足$f(a)<u<f(b)$或 $f(a)>u>f(b)$），则至少存在一点 $c∈(a,b)$，使得$f(c)=u$

- **费马引理（极值点导数为0）**：若 $f(x)$ 在 $x_0$ 处可导，且在 $x_0$ 的某邻域内有 $f(x) \le f(x_0)$（或 $\ge$），则 $f'(x_0) = 0$

- **1. 罗尔定理**：  
	- 若 $f\in C[a,b]$ 且在 $(a,b)$ 可导，$f(a)=f(b)$，则存在 $\xi \in (a,b)$ 使 $f'(\xi)=0$。
	- 推广：$\lim f(a) = \lim f(b)$，则存在

- **2. 拉格朗日定理**：  
	- 若 $f\in C[a,b]$ 且在 $(a,b)$ 可导，则存在 $\xi \in (a,b)$ 使：
$$
f'(\xi) = \frac{f(b)-f(a)}{b-a}
$$

	- 在使用取点时，可以用待定系数法，取得具备特定性质的点
	- 双取点问题

- **3. 柯西定理**：  
	- 若 $f,g\in C[a,b]$ 且在 $(a,b)$ 可导，$g'(x) \neq 0$，则存在 $\xi \in (a,b)$ 使：
$$
\frac{f'(\xi)}{g'(\xi)} = \frac{f(b)-f(a)}{g(b)-g(a)}
$$

- **4. 泰勒定理**：  
$$
f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!} (x-x_0)^k + R_n(x)
$$
	- 其中余项 $R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x-x_0)^{n+1} \ (\xi \text{ 在 } x_0,x\text{ 之间})$。
 

##### 积分中值定理

- **积分第一中值定理**： 若 $f(x) \in C[a,b]$，则存在 $\xi \in [a,b]$ 使： $$\int_a^b f(x) dx = f(\xi)(b - a)$$ - 推广：若 $g(x)$ 在 $[a,b]$ 上不变号，则存在 $\xi \in [a,b]$ 使： $$\int_a^b f(x)g(x) dx = f(\xi) \int_a^b g(x) dx$$
- **积分第二中值定理**： 若 $f(x)$ 在 $[a,b]$ 上单调，$g(x) \in C[a,b]$，则存在 $\xi \in [a,b]$ 使： $$\int_a^b f(x)g(x) dx = f(a) \int_a^\xi g(x) dx + f(b) \int_\xi^b g(x) dx$$
##### 证明导数值为0

- 罗尔中值定理，证明$f(a)=f(b)$
- 推广的罗尔中值定理：开区间，证明$\lim f(a) = \lim f(b)$，实际上由介值定理，可以保证取到其他函数值相同的点
- 利用极值点：构造闭区间，且区间上存在极值


---

### 单变元积分

#### 基本积分公式

熟悉的：
$$
\begin{aligned} \int x^n \, dx &= \frac{x^{n+1}}{n+1} + C \quad (n \neq -1) \\ \int \frac{1}{x} \, dx &= \ln |x| + C \\ \int e^x \, dx &= e^x + C \\ \int a^x \, dx &= \frac{a^x}{\ln a} + C \quad (a>0,\ a\neq1) \\\int sin x \, dx &= -cos x + C \\ \int \frac{1}{\sqrt{1-x^2}} \, dx &= arcsin x + C \\\int \frac{1}{\sqrt{a^2 - x^2}} \, dx &= arcsin \frac{x}{a} + C \\\int \frac{1}{1+x^2} \, dx &= arctan x + C \\ \int \frac{1}{a^2 + x^2} \, dx &= \frac{1}{a} arctan \frac{x}{a} + C \\ 
\end{aligned}
$$

不太熟悉，关于三角的，最后一个尤其注意$$\begin{aligned} \int tan x \, dx &= -\ln |cos x| + C \\ \int cot x \, dx &= \ln |sin x| + C \\ \int sec^2 x \, dx &= tan x + C \\ \int csc^2 x \, dx &= -cot x + C 
 \\ \int sec x \, dx &= \ln |sec x + tan x| + C \\ \int csc x \, dx &= \ln |csc x - cot x| + C \\  
\int sec^3 x \, dx &= \frac{1}{2} sec x tan x + \frac{1}{2} \ln|sec x + tan x| + C\\\int sinh x \, dx &= cosh x + C \\ \int cosh x \, dx &= sinh x + C \\\int \frac{dx}{\sqrt{x^2 \pm a^2}} &= \ln |x + \sqrt{x^2 \pm a^2}| + C\\
\end{aligned}$$
学会推导 $sec^{3}$ 的积分：$$\begin{align}
&\int sec^{3}x dx=\int sec x \; d(tan x) \\ &=  tan x sec x - \int tan^{2}x sec x dx \\&= tan x sec x - \int (1-sec^{2}x)sec x dx 
\end{align}$$
#### 积分技巧
##### 常见凑微分方式
$$
\begin{aligned} &\int f(ax+b) \, dx = \frac{1}{a}\!\int f(ax+b)\,d(ax+b) \\\ &\int x^{n-1}f(x^n)\,dx = \frac{1}{n}\!\int f(x^n)\,d(x^n) \\\ &\int e^{x}f(e^{x})\,dx = \int f(e^{x})\,d(e^{x}) \\\ &\int \frac{f(\ln x)}{x}\,dx = \int f(\ln x)\,d(\ln x) \\\ &\int cos x\,f(sin x)\,dx = \int f(sin x)\,d(sin x) \\\ &\int sin x\,f(cos x)\,dx = -\!\int f(cos x)\,d(cos x) \\\ &\int sec^2 x\,f(tan x)\,dx = \int f(tan x)\,d(tan x) \\\ &\int \frac{dx}{\sqrt{a^{2}-x^{2}}} = arcsin\frac{x}{a}+C \end{aligned}
$$

##### 常见换元方式
**三角代换**：
   - $\sqrt{a^2-x^2}$：令 $x = a sin t$
   - $\sqrt{a^2+x^2}$：令 $x = a tan t$
   - $\sqrt{x^2-a^2}$：令 $x = a sec t$
   - **万能三角代换**：$t= tan (\frac{x}{2})$

**其他代换**：
   - 出现较多$tan x$与$sec x$，令$u=tan x$，$du=tan^{2}x dx$，代入变换积分，
   - **根式代换**：当被积函数中含有根式（如 $\sqrt{ax+b​}$）时，可令整个根式为新变量，以消除根号
   
 **倒代换**：适合分母比分子次数更高的时候

##### 多项式的分部积分
$$
\boxed{\int u\,dv = uv - \int v\,du}
$$

多项式 P(x)的导数会降低次数
1. $\int P(x)e^{ax}\,dx$     设 $u = P(x)$，$dv = e^{ax}\,dx$
2. $\int P(x)sin(bx)\,dx$  设 $u = P(x)$，$dv = sin(bx)\,dx$ 或 $dv = cos(bx)\,dx$

对数函数 $lnx$的导数为 $\frac{1}{x}$​，会转化为代数函数。
1. $\int P(x)\ln x\,dx$   设 $u = \ln x$，$dv = P(x)\,dx$
2. 同理$arctan x$也是，化为代数函数

循环积分：两次分部积分后还原
1. $\int e^{ax}sin(bx)\,dx \quad\text{或}\quad \int e^{ax}cos(bx)\,dx$ ，设 $u=e^{ax}$，$dv=sin (bx)dx$，两次分部积分

其他：
- 反三角混合指数，果断分部积分


##### 其他积分技巧

- **区间再现公式**：$\int^{a}_{0}​f(x)dx=\int^{a}_{0}f(a−x)dx$：
 $$
\int_{0}^{1} x(1-x)^9 \, dx \xlongequal{1-x=t} \int_{0}^{1} (1-t) t^9 \, dt = \frac{1}{110},
$$
	- 尤其对于三角函数
	- $t=\pi-x$，不改变三角名称，也许可以平移区间
	- $t= \frac{\pi}{2} - x$，转化 $sin$ 与 $cos$


- 三角的幂，$\int sin^{m}x cos^{n}x dx$
	- 如果 $m$为奇数：令 $u=cosx$，利用 $sin^{2}x=1−cos^{2}x$，化为$\int -u^{n}(1-u^{2})^{\frac{m-1}{2}}du$
	- 如果 $n$为奇数：令 $u=sinx$，
	- 如果都是偶数：使用倍角公式降幂


#### 有理函数分解的留数法

对真分式 $\int \frac{P(x)}{Q(x)} dx$，当 $Q(x)$ 可分解为 $(x-a_1)^{k_1} \cdots (x-a_m)^{k_m}$ 时，可用 **留数法** 快速求部分分式系数： 

1. **单极点情形**（$k_i=1$）： $$A_i = \lim_{x \to a_i} (x-a_i) \frac{P(x)}{Q(x)} = \frac{P(a_i)}{Q'(a_i)}$$ 其中 $Q'(x)$ 是分母的导数。 

2. **重极点情形**（$k_i>1$）： 设 $(x-a)^k$ 为重因式，则系数 $A_j$（$j=1,\cdots,k$）为： $$A_j = \frac{1}{(k-j)!} \lim_{x \to a} \frac{d^{k-j}}{dx^{k-j}} \left[ (x-a)^k \frac{P(x)}{Q(x)} \right]$$ 分母次数越高，求导次数越少

在实数域内，复极点(**不可约的二次因式**)不能分解，改为$$\frac{P_n(x)}{Q_m(x)} = \sum \left[ \frac{A}{x-a} + \cdots + \frac{Mx+N}{x^2+px+q} \right]$$

#### Wallis公式

用于 $\int_0^{\pi/2} sin^n x \, dx$ 或 $\int_0^{\pi/2} cos^n x \, dx$：
$$
W_n = \begin{cases}
\dfrac{(n-1)!!}{n!!} \cdot \dfrac{\pi}{2} & n \text{ 偶} \\
\dfrac{(n-1)!!}{n!!} & n \text{ 奇}
\end{cases}
$$
其中 $n!!$ 表示双阶乘。

对偶次幂，$sin^{n}(kx) dx$ 的结果与$sin^{n}(x) dx$ 一致

#### 定积分的几何应用

注意下面的是$y=f(x)$**与其他曲线围成的二维图形**，旋转后形成旋转体。一定要找准二维图形。

- **圆盘法**：适合当切片垂直于旋转轴时，切片是圆盘或圆环。在图形**与旋转轴相邻**时简单，就是圆盘。否则要转化为圆环（加减）
	- 绕x轴旋转，且图形由y=f(x)和x轴围成 → 圆盘法简单
	- 绕y轴旋转，且图形由x=g(y)和y轴围成 → 圆盘法简单
- **柱壳法**：适合当切片平行于旋转轴时，切片为圆柱壳
	- 绕y轴旋转，但图形由y=f(x)和x轴围成 → 柱壳法更直接
	- 绕x轴旋转，但图形由x=g(y)和y轴围成 → 柱壳法更直接


![旋转体体积](/Notes-for-GradEntranceExam/微积分笔记/assets/微积分公式结论汇总/DA217D4713EC13C14BEEF1E961F615AA.png)

| 旋转轴 | 方法  | 体积公式                                  |
| --- | --- | ------------------------------------- |
| x轴  | 圆盘法 | $V_x = \pi \int_a^b [f(x)]^2 dx$      |
| x轴  | 柱壳法 | $V_x = 2\pi \int_c^d y \cdot g(y) dy$ |
| y轴  | 圆盘法 | $V_y = \pi \int_c^d [g(y)]^2 dy$      |
| y轴  | 柱壳法 | $V_y = 2\pi \int_a^b x \cdot f(x) dx$ |


##### 弧长公式

本质上是$ds=\sqrt{(dx)^{2}+(dy)^{2}}$

1. 直角坐标 $y = f(x)$：$L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx$
2. 参数方程 $x(t), y(t)$： $L = \int_\alpha^\beta \sqrt{[x'(t)]^2 + [y'(t)]^2} \, dt$
3. 极坐标方程$r(\theta),\theta$：$x=r(\theta)cos(\theta)$ 代入微分关系$$
L = \int_{\theta_1}^{\theta_2} \sqrt{\left(\frac{dr}{d\theta}\right)^2 + r^2} \, d\theta
$$
##### 旋转曲面的侧面积

注意考虑旋转曲面时，我们**只考虑$f(x)$曲线本身**，而不是某个二维区域！

这意味着公式求取的侧面积不包括：
- 底面和顶面（如果是封闭曲面）
- 其他边界平面

小段弧长很小时，带状曲面可以近似看作一个圆台的侧面。圆台的侧面积公式是：π×(上底面半径+下底面半径)×母线长

| 旋转轴 | 表面积公式                 |
| --- | --------------------- |
| x轴  | $S = \int 2\pi y\;ds$ |
| y轴  | $S = \int 2\pi x\;ds$ |

##### 形心公式（质心）

实际上这只是把一般的二维质心公式的二重积分展开为定积分，还只对下曲线为$y=0$成立……
$$
\bar{x} = \frac{\int_a^b x f(x) \, dx}{\int_a^b f(x) \, dx}, \quad 
\bar{y} = \frac{\int_a^b \frac{1}{2}[f(x)]^2 \, dx}{\int_a^b f(x) \, dx}
$$

#### 反常积分

- 判断反常积分：找瑕点、无穷区间
- 瑕积分：$\int_a^b f(x)dx = \lim_{t \to c^-} \int_a^t f(x)dx + \lim_{t \to c^+} \int_t^b f(x)dx$  (**要求两个极限均存在才收敛**)
- 含多个反常点必须拆分，而且要求每一个都收敛

标准积分：P积分
**比较判别法**：其他积分首先尝试，在靠近瑕点的地方能否与p积分类比（泰勒）。但注意，只适合**非负函数**

| 类型                                  | 收敛条件    | 发散条件       |
| :---------------------------------- | :------ | :--------- |
| $\int_1^{+\infty} \frac{1}{x^p} dx$ | $p > 1$ | $p \leq 1$ |
| $\int_0^1 \frac{1}{x^p} dx$         | $p < 1$ | $p \geq 1$ |

**狄利克雷判别法**
- 判别形如 $\int_a^{+\infty} f(x)g(x) dx$ 的积分，多用于振荡被积函数
    *   **条件**：
        1.  $g(x)$ **单调**且 $\lim_{x \to +\infty} g(x) = 0$。
        2.  $f(x)$ 的**积分有界**，即 $\left| \int_a^b f(x) dx \right| \leq M$ (对任意$b>a$)。
    *   **结论**：积分收敛。
    *   举例：$\int^{\infty}_{1} \frac{sin x}{x}$

##### 含有对数的积分

核心思路：**转化为类似gamma函数**：

$$令 u=lnx，则 du= \frac{1}{x}dx，积分化为\int^{\infty}_{ln 2} \frac{1}{u^{q}(e^u)^{p-1}} \;du$$
则有结论：$$\begin{align}
& \int^{0}_{\infty} t^{n}e^{- \alpha t}dt \;收敛 \iff n>-1 \\
& \int^{a}_{\infty} t^{n}e^{- \alpha t}dt \;收敛 \iff a>0, \alpha>0, \forall n 
\end{align}$$
记住一些常见结论：

- 趋于无穷总是发散（$\frac{1}{\ln x} > \frac{1}{x}$）
$$\int_2^\infty \frac{1}{\ln^{p}(x)} dx$$
- 趋于0总是收敛（换元，其实就是$\Gamma$函数）
$$\int_0^{0.5} | \ln(x)|^{p} dx$$
- 趋于1时，要求$p<1$（**等价为 $p$ 级数**，$x$ 趋于0）
$$\int_{0.5}^{1} \frac{1}{| \ln(x)|^{p}} dx$$


1. $\int_2^{+\infty} \frac{1}{x^p (\ln x)^q}  dx$

	注意 $p=1,q>1$，收敛。$p>1, \forall q$，也收敛


2. $\int_1^{2} \frac{1}{x^p (\ln x)^q}  dx$

	只有1是瑕点，此时$x^{p}$不起作用，$\ln x \sim (x-1)$，收敛条件：$q < 1$，**等价为p级数**

3. $\int_0^1 \frac{1}{x^p |\ln x|^q}  dx$

	有两个瑕点，要求两个积分都收敛。事实上是
$$令 u=lnx，则 du= \frac{1}{x}dx，积分化为\int^{0}_{- \infty} \frac{1}{u^{q}(e^u)^{p-1}} \;du$$

	趋于1时，对对数部分，要求$q<1$；
	趋于0时，对整体，由于$x^{p}\ln x = x^{p}$，**对数部分无影响**，于是要求$p<1$

4.  $\int_0^1 \frac{|\ln x|^q}{x^p }  dx$

	**对数在分子，只要$q>-1$，就是p积分，对数部分无影响**

### 级数

#### 敛散性相关的特例、判别

##### 正项级数

- **观察部分和 $S_{n}$**
	- 单调有界：$\sum u_n (u_n \geq 0)$ 收敛 $\iff$ 部分和序列 $\{S_n\}$ 有上界
	- 尤其是$a_{n}$具有差值结构的时候，telescoping求和
- 比较判别法
	- 注意**比较判别法只适合正项级数**！
	- 常用极限形式


比值法和根值法本质上是通过考察级数的绝对值（即**绝对收敛**）来判断收敛性，适合所有级数
- 比值判别法：设 $\lim_{n \to \infty} \dfrac{u_{n+1}}{u_n} = \rho$：
$$\begin{cases}
\text{收敛} & \rho < 1 \\
\text{发散} & \rho > 1 \\
\text{不确定} & \rho = 1
\end{cases}$$
- 根式判别法：设 $\lim_{n \to \infty} \sqrt[n]{u_n} = \rho$：
$$\begin{cases}
\text{收敛} & \rho < 1 \\
\text{发散} & \rho > 1 \\
\text{不确定} & \rho = 1
\end{cases}$$
- 无论是比值法还是根值法，都**只是充分条件**，而不是必要条件。极限不一定存在


积分判别法
- **积分判别法**：
	1. 函数f(x)在区间$[N, \infty)$上连续，其中$N$为某个整数。
	2. $f(x)$为正。
	3. $f(x)$递减。
	4. $f(n) = a_n$对于所有$n ≥ N$。
    - 如果这些条件满足，那么级数$∑a_n$和积分$\int^{N}_{\infty} f(x) dx$同时收敛或发散。

**拉贝尔判别法**：当比值法极限为1时使用
$$
\lim_{n \to \infty} n \left(1 - \frac{u_{n+1}}{u_n}\right) = \rho > 1\;则收敛
$$

##### 交错级数

- 莱布尼茨判别法：若 $u_n > 0$ 满足：
	1. $u_n \geq u_{n+1}$（单调不增）
	2. $\lim_{n \to \infty} u_n = 0$  
	- 则交错级数 $\sum_{n=1}^{\infty} (-1)^{n-1} u_n$ 收敛

- 用比值法和根值法看是否绝对收敛


绝对收敛相关
- $\sum a_n$收敛，$\sum b_{n}$收敛，且其中至少有一个绝对收敛 $\implies \sum a_{n}b_{n}$收敛
- 绝对收敛的级数其所有子级数也收敛

#### 幂级数

##### 幂级数的收敛

$$\sum a_{n}f^{n}(x)$$

幂级数的收敛半径核心是正项级数里的两个式子,**将通项视为整体**：
- 令$\lim_{n \to \infty} \dfrac{a_{n+1}f^{n+1}(x)}{a_{n}f^{n}(x)} < 1$
- 令$\lim_{n \to \infty} (a_{n}f^{n}(x))^\frac{1}{n} < 1$


---

**标准形式**的幂级数：$$\sum a_{n}x^{n}$$
$f(x)=x$，则可以导出不含$x$的式子：
*   柯西-阿达玛公式：
    $$R = \frac{1}{\limsup_{n \to \infty} \sqrt[n]{|a_n|}}$$
	- 上极限一定是$R$
*   达朗贝尔判别法：
 $$
\frac{1}{\limsup_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|} \leq R \leq \frac{1}{\liminf_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|}
$$
	- **不能**简单地将比值法的上极限直接等于 $1/R$
	- 如果极限存在，则取等：注意这里**允许比值为1**
    $$\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lambda \Rightarrow R = \frac{1}{\lambda}$$

##### 缺项幂级数

- 缺奇次项/偶次项，可以变量替换，转化为不缺项幂级数
	- 于是可以用上面的两个公式
- 大幅缺项，如$\sum a_{n}x^{n^{2}}$，不能转化为不缺项，只能按照定义求


##### 幂级数的和函数

基本的式子
$$\begin{aligned}
e^x &= \sum_{n=0}^{\infty} \frac{x^n}{n!} \\
sin x &= \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} \\
\frac{1}{1-x} &= \sum_{n=0}^{\infty} x^n \quad (|x|<1)\\
    &\sum_{n=0}^{\infty} x^n = \frac{1}{1-x} \quad (|x| < 1) \\
    &\sum_{n=1}^{\infty} n x^{n-1} = \frac{1}{(1-x)^2} \\
    &\sum_{n=1}^{\infty} \frac{x^n}{n} = -\ln(1-x)\\
\end{aligned}$$

- 两个幂级数相加、相乘后，新的收敛半径可能**大于等于**原收敛半径的最小值。
- 除法：收敛半径可能变小
- 幂级数逐项求导、积分后，收敛半径不变（但端点收敛性可能改变）
- 在收敛域内，幂级数绝对收敛
	- 其任意子级数也绝对收敛
- 在端点处，幂级数可能条件收敛，可能发散
	- 子级数也无法判别
- 事实上，**奇次项级数的收敛半径总是大于或等于原级数的收敛半径**，因为它可以由原级数运算得到


#### 积累例子

- $a_{n}=\dfrac{u_{n}-u_{n-1}}{\sqrt{u_{n}}}$，差分结构，但是根式破坏了求和关系，可以放缩掉。
	- 令$\sqrt{u_{n}}=v_{n}$，则$a_{n}=\dfrac{(v_{n}+v_{n-1})(v_{n}-v_{n-1})}{v_{n}}$
	- 如果$u_{n}$为正，且单调递减，则$u_{n}$极限存在，可放缩掉$\dfrac{(v_{n}+v_{n-1})}{v_{n}}$
- 有理化操作，实际上估计阶次就够了$$\begin{align*}
\frac{(\sqrt{n+1}-\sqrt{n})^p}{n} &= \frac{1}{n(\sqrt{n+1}+\sqrt{n})^p} \sim \frac{1}{2^p \cdot n^{\frac{1+p}{2}}}, \\
\frac{1}{n^p} - \frac{1}{(n+1)^p} &= \frac{(n+1)^p - n^p}{n^p(n+1)^p} \sim \frac{pn^{p-1}}{n^{2p}} = \frac{p}{n^{p+1}}, \\
\frac{\sqrt{n+2}-\sqrt{n-2}}{n^a} &= \frac{4}{n^a(\sqrt{n+2}+\sqrt{n-2})} \sim \frac{2}{n^{\frac{a+1}{2}}}.
\end{align*}$$
- 常见举例函数
	- $\dfrac{1}{n}$、$\dfrac{\ln n}{n}$，发散
	-
- 用上极限求得$\sum a_{n}x^{n}$ 收敛半径是$0.5$：$$
a_n = 
\begin{cases} 
1, & n \text{ 为偶数} \\ 
2^n, & n \text{ 为奇数}
\end{cases}
$$
- 原幂级数收敛，奇次项构成的幂级数发散：$\sum \dfrac{(-1)^{n}}{n} x^n$在$x=1$处


#### 傅里叶级数

$f(x)$ 在 $[-T/2, T/2]$ 上的Fourier展开：
$$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n cos \frac{2n\pi x}{T} + b_n sin \frac{2n\pi x}{T} \right)$$
系数：
$$a_n = \frac{2}{T} \int_{-T/2}^{T/2} f(x)cos n\omega \, xdx$$
$$b_n = \frac{2}{T} \int_{-T/2}^{T/2} f(x)sin n\omega \, x dx$$
和函数$S(x)$：$$S(x) = 
\begin{cases} 
f(x), & x \text{ 为连续点}, \\
\dfrac{f(x-0) + f(x+0)}{2}, & x \text{ 为间断点}, \\
\dfrac{f(-l+0) + f(l-0)}{2}, & x = \pm l，l为半周期.
\end{cases}$$
注意看题目是**求级数，还是和函数**





### 多元微分

#### 二元函数的连续、可导、可微

##### 一组关系

在多元函数中，**在某点偏导数存在 与 在某点连续 没有蕴含关系**，可微 比 偏导数存在 更强

$$
f(x, y) = 
\begin{cases} 
\frac{xy}{x^2 + y^2}, & (x, y) \neq (0, 0) \\
0, & (x, y) = (0, 0)
\end{cases}
$$

---

仅考察可积、连续和可微，由弱到强：
- 可积、连续、在$x_{0}$可微（全微分），在邻域上可微、连续可微（一阶偏导数连续）、在$x_{0}$二阶可微……

考察导数和可微
- 部分方向导数存在（如$x \to 0^{-}$）、偏导数存在（沿轴的方向的**双向导数**）、所有方向导数存在、在$x_{0}$可微（全微分/梯度）、偏导数连续……
- $f^{'}_{x}(0,0)$存在（在一个点） < $f^{'}_{x}(0,y)$存在（在一条线上）< $f^{'}_{x}(x,y)$存在（全平面）


混合偏导数（在考研范围不研究充要条件）
- 二阶偏导数连续 $\implies$ 在邻域上二阶可微 $\implies$ 在邻域上混合偏导数相等
- 混合偏导数相等 **不足以** 推出函数在某点可微（哪怕一阶可微）


> 一元：由弱到强 可积、连续、在$x_{0}$点可导、在邻域上可导、连续可导（导函数连续）

---

##### 计算

求偏导（一元极限）
- 求全平面偏导：
	- 用定义（少见）$$
f_x(x, y) = \lim_{h \to 0} \frac{f(x + h, y) - f(x, y)}{h}
$$
	- 求导法则直接求
- 求某点偏导（提前代入再用定义，通常简单）：$$
f_x(b, a) = \lim_{h \to 0} \frac{f(b + h, a) - f(b, a)}{h}
$$
- 验证偏导数在某点连续
	- 首先求偏导在邻域内的形式
	- 再求偏导数在该点的值
	- 验证连续性（二重极限）


判定可微（二重极限）
- 偏导数连续 $\implies$ 可微
- 先求必要条件：在点的偏导数存在
- 再按照定义验证（二重极限），注意是$\Delta f$ $$\lim_{\rho\to 0}\frac{\Delta f-[f_x'(x_0,y_0)\Delta x+f_y'(x_0,y_0)\Delta y]}{\rho}=0,\\;\rho=\sqrt{\Delta x^{2}+ \Delta y^{2}}$$
- 二重极限求解
	- 极坐标代换，$x = a + rcos\theta,\\quad y = b + rsin\theta \\quad (r \to 0^+)$，$\lim_{r\to0} f(r,\theta)$ **存在且与** $\theta$ **无关** $\implies$极限存在  
		- 这意味着幂次分析：若 $\lim \sim r^k \phi(\theta)$：  
	     - $k > 0$：极限为 0  
	     - $k < 0$：极限不存在  
	     - $k = 0$：需检查 $\phi(\theta)$ 是否常数
	 - 夹逼$$\begin{aligned}
     &x^2 + y^2 \geq 2|xy| \\
     &|x| \leq r, |y| \leq r \\
     &|sin\theta|, |cos\theta| \leq 1
     \end{aligned}$$
     - 有界量 * 无穷小：$f(x,y) = \underbrace{g(x,y)}_{\text{有界}} \times \underbrace{h(r)}_{\to 0}$
- 二重极限不存在
	- 特殊路径，通常考虑分母
	- 取同阶：$x^{n}+y^{m}$，取$y=x^\frac{n}{m}$，尤其适合齐次式
	- 升阶：$x+y$，取$y=-x+x^{2}$
	- 震荡：$y=x sin \frac{1}{x}$



##### 隐函数

隐函数定理：若 $F$在 $(x0​,y0​,z0​)$连续可微（即 $F∈C1$），且偏导数 $Fz​(x0​,y0​,z0​)  \neq 0$，则：
- 存在唯一隐函数$z=z(x,y)$在 $(x0​,y0​)$附近。
- $z(x,y)$连续可导


#### 极值问题

##### 无约束极值

海塞矩阵的正定与负定
- 正定：极小值
- 负定：极大值
- **不定：非极值**（判别方法是行列式为负）
- 不满秩：方法失效（至少有一个特征值为零。这表明在某个方向上，二阶导数为零）
$$\begin{bmatrix}
A, B\\ B, C \\
\end{bmatrix}$$

| $AC-B^2$ | $A$  | 结果  |
| -------- | ---- | --- |
| $>0$     | $>0$ | 极小值 |
| $>0$     | $<0$ | 极大值 |
| $<0$     | 任意   | 非极值 |
| $=0$     | 任意   | 不定  |

##### 约束极值

多元函数极值的存在性定理：如果函数在**有界闭集（即紧集）** 上连续，那么函数在该区域上一定取得最大值和最小值。这里的关键是区域必须是“有界”且“闭”的，即紧集。

在考研数学里，将约束分为了等式约束和不等式约束
- 等式约束$g(x)=0$：
	- $n$维空间里的一个$n-1$维部分，比如平面上的曲线、空间中的平面
	- 等式约束一定是**闭区域**
	- 区域可能是**无界**的$y-x=2$，也可能是**有界**的$x^{2}+y^{2}+z^{2}=1$
	- 使用拉格朗日乘子法求解
	- **偏导不存在的点**单独考虑
- 不等式约束$g(x)<=0$
	- $n$维空间里的一个$n$维子部分
	- 开闭性
		- $g(x)<=0$，闭集
		- $g(x)<0$，开集
	- 有界性
		- 看$g(x)=0$
	- 求解
		- 在**区域内部，不存在约束**，退化为无约束极值，但注意是**开区域**
		- 区域边界（等式约束部分），拉格朗日乘子法
- 事实上可以由互补松弛条件整合


然而**极值是否一定存在**，重点是看区域的**有界性**（紧致）和开闭性
- 区域是有界且闭的，则必存在最值
	- 举例：等式约束$x^{2}+y^{2}+z^{2}=1$，连续函数在该区域必然有最值（不一定是极值点）
	- 举例：不等式约束$x^{2}+y^{2}+z^{2}<=1$，区域是闭的且有界的
- 区域是有界且开的，不一定存在
	-  举例：$x^{2}+y^{2}<1$，求$z(x,y)=x^{4}+y^{2}$
	- 如果遇到这种问题，如果内部有极值点，为了表明内部是否是最值，**需要求出边界上的最值**，与内部的判别（因为内部点可以无限靠近边界点）
	- 比如上式，内部有极小值$0$，验证边界有最小值$\frac{3}{4}$，相当于下确界，故内部是极值
- 区域是无界的，不一定有最值
	- 举例：$y-x=1$，求$z(x,y)=x^3+y^3$



#### 场相关

*   **数量场**：$\varphi(M)=\varphi(x,y,z)$  ，常见的多元函数是数量场
*   **矢量场**：$\vec{A}(M)=(P,Q,R)$

##### 方向导数
方向导数$\frac{\partial f}{\partial\vec{l}}$计算：
$$\begin{align}
\frac{\partial f}{\partial\vec{l}}&=f_x'cos\alpha+f_y'cos\beta+f_z'cos\gamma\\
&= \frac{\nabla f \cdot \vec{l}}{|\vec{l}|}\quad \text{如果可微}
\end{align}$$
$\vec{l}$ 方向单位向量$(cos\alpha,cos\beta,cos\gamma)$


##### 三种重要的算子

| 运算              | 输入（操作对象） | 输出（结果） | 通俗理解                 |
| --------------- | -------- | ------ | -------------------- |
| 梯度 (Gradient)   | 数量场      | 矢量场    | 描述数量场中变化最快的方向和速率。    |
| 散度 (Divergence) | 矢量场      | 数量场    | 描述矢量场在某点的“源”或“汇”的强度。 |
| 旋度 (Curl)       | 矢量场      | 矢量场    | 描述矢量场在某点的旋转程度和旋转轴。   |

##### 梯度

对标量场$f=f(x,y,z)$
$$\mathbf{grad}f=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\right)=\nabla f$$
**方向导数=梯度在$\vec{l}$方向投影**

对矢量场，可以拓展为雅可比：$$J = \begin{bmatrix}
\nabla f_{1}\\ \nabla f_{2}\\  \nabla f_{3}\\ \dots \\
\end{bmatrix}$$

##### 散度 (Divergence)  
* **定义**：对矢量场 $\vec{A}(M)=(P(x,y,z),Q(x,y,z),R(x,y,z))$  
  $$\text{div} \vec{A} = \nabla \cdot \vec{A} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}=tr(J)$$
##### 旋度 (Curl)
* **定义**：对矢量场 $\vec{A}(M)=(P(x,y,z),Q(x,y,z),R(x,y,z))$  
  $$\text{curl} \vec{A} = \nabla \times \vec{A} = \begin{vmatrix}
  \vec{i} & \vec{j} & \vec{k} \\
  \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
  P & Q & R
  \end{vmatrix}$$