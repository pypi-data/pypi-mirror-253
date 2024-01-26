from lark import Lark, Transformer, LarkError

latex_maths_grammar = """
    start: "$" command "$" | "\\\\[" command "\\\\]"
    command: frac | sqrt | power | subscript | equality | addition | subtraction | multiplication | vector | unit_vector | scalar_vector | cross_product | dot_product | product | milli_ampere | volts | seconds | speed | WORD | INTEGER | DECIMAL | latex_command | sin | cos | tan | cot | sec | cosec | theta | integral | leq | rho | text | less_than | pi | cdot | times | epsilon | dx | ohm | delta | circular_integral | x | meter | tesla | ampere | newton | mod | pause | SIGNED_DECIMAL | SIGNED_INTEGER | mu | quad | otimes | centimeter | by | ratio | degree | phi
    frac: "\\\\dfrac{" command "}{" command "}"
    sqrt: "\\\\sqrt{" command "}"
    power: command "^" command | command "^" "{" command "}"
    subscript: command "_" command | command "_{" command "}" | command "_{" WORD "}"
    equality: "="
    addition: command "+" command
    subtraction: command "-" command
    multiplication: command "*" command
    vector: "\\\\vec{" command "}" | "\\\\vec{" WORD "}" 
    unit_vector: "\\\\hat{" WORD "}"
    scalar_vector: DECIMAL vector | INTEGER vector
    cross_product.2: vector "\\\\times" vector | "\\\\times" vector | vector "\\\\times" unit_vector 
    dot_product: vector "\\\\cdot" vector
    product: command command+ | WORD "\\\\cdot" command | command "\\\\cdot" command | WORD "\\\\times" command | WORD command 
    
    
    leq: "\\\\leq" 
    rho: "\\\\uprho" | "\\\\rho" | "\\\\rho_" (WORD | INTEGER) | "\\\\uprho_" (WORD | INTEGER)
    text: "\\\\text{" command "}" | "\\\\textit{" command "}" | "\\\\textbf{" command "}" | "\\\\textsc{" command "}" | "\\\\texttt{" command "}" | "\\\\textsf{" command "}"
    less_than: "<" | "\\\\textless"
    pi: "\\\\pi"
    mod: "|" command "|" | "\\\\left|" command "\\\\right|"
    cdot: "\\\\cdot"
    times: "\\\\times"
    epsilon: "\\\\epsilon" | "\\\\varepsilon" | "\\\\epsilon_" (WORD | INTEGER)
    mu: "\\\\upmu_" (WORD | SIGNED_INTEGER) | "\\\\mu_" (WORD | SIGNED_INTEGER) | "\\\\mu"
    quad: "\\\\quad"
    otimes: "\\\\otimes"
    
    
    dx: "\\\\d{" (WORD | command) "}"
    
    delta: "\\\\delta" | "\\\\Delta"
    x: "x"
    
    
    
    
    
    sin: "\\\\sin" "{" command "}" | "\\\\sin" command | "\\\\sin" "(" command ")" | "\\\\sin" "\\\\left(" command "\\\\right)"
    cos: "\\\\cos" "{" command "}" | "\\\\cos" command | "\\\\cos" "(" command ")" | "\\\\cos" "\\\\left(" command "\\\\right)"
    tan: "\\\\tan" "{" command "}" | "\\\\tan" command | "\\\\tan" "(" command ")" | "\\\\tan" "\\\\left(" command "\\\\right)"
    cot: "\\\\cot" "{" command "}" | "\\\\cot" command | "\\\\cot" "(" command ")" | "\\\\cot" "\\\\left(" command "\\\\right)"
    sec: "\\\\sec" "{" command "}" | "\\\\sec" command | "\\\\sec" "(" command ")" | "\\\\sec" "\\\\left(" command "\\\\right)"
    cosec: "\\\\cosec" "{" command "}" | "\\\\cosec" command | "\\\\cosec" "(" command ")" | "\\\\cosec" "\\\\left(" command "\\\\right)"
    
    theta: "\\\\theta"
    integral.2: "\\\\int" ("_" command "^" command)? command "\\\\d{" WORD "}" | "\\\\int" ("_" command "^" command)? command
    circular_integral: "\\\\oint" 
    
    
    milli_ampere: "\\mA"
    volts: "\\V"
    seconds: "\\s"
    speed: "\\mps"
    ohm: "\\Ohm" | "\\Omega"
    meter: "\\m"
    tesla: "\\Tesla" | "\\T"
    ampere: "\\Amp"
    newton: "\\N"
    centimeter: "\\cm"
    by: "/"
    ratio: ":"
    degree: "^\\\\circ"
    phi: "\\\\phi"
    
    latex_command: "\\\\" WORD
   
    pause: "[[slnc " SIGNED_INTEGER "]]"
     
    DECIMAL: /\d+\.\d+/
    INTEGER: /\d+/
    SIGNED_INTEGER: /-?\d+/
    SIGNED_DECIMAL: /-?\d+\.\d+/
    
    
    LETTER: /[a-zA-Z]/
    WORD: /[a-zA-Z]+/
    DOLLAR: "$"
    ANY: "\\\\" WORD | "\\\\" WORD+
    %ignore " " 
    %ignore "&" 
    %ignore "("
    %ignore ")"
    %ignore "\\\\left(" | "\\\\right)"
"""
#%ignore /\\\\\\\\\[\d+mm\]/
#definite_integral: "\\\\int" "^" command "_" command command "\\\\d{" command "}" | "\\\\int" "_" command "^" command command "\\\\d{" command "}"


class LaTeXTransformerMaths(Transformer):
    def frac(self, items):
        return f"{items[0]} upon {items[1]}"

    def sqrt(self, items):
        return f"square root of {items[0]}"

    def power(self, items):
        if items[1] == "2":
            return f"{items[0]} squared"
        elif items[1] == "3":
            return f"{items[0]} cubed"
        elif items[1] == "0.5":
            return f"{items[0]} to the power of half"
        else:
            return f"{items[0]} to the power of {items[1]}"

    def subscript(self, items):
        return f"{items[0]} {items[1]}"

    def equality(self, items):
        return f"equals to "

    def addition(self, items):
        return f"{items[0]} plus {items[1]}"

    def subtraction(self, items):
        return f"{items[0]} minus {items[1]}"

    def multiplication(self, items):
        return f"{items[0]} times {items[1]}"

    def vector(self, items):
        return f"vector {items[0]}"
    
    def unit_vector(self, items):
        return f"{items[0]} cap "
    
    def scalar_vector(self, items):
        return f"{items[0]} times {items[1]}"
    
    def cross_product(self, items):
        if items[0] == "times":
            return f"cross {items[1]}"
        else:
            return f"{items[0]} cross {items[1]}"
    
    def dot_product(self, items):
        return f"{items[0]} dot {items[1]}"

    def product(self, items):
        return "   ".join(str(item) for item in items)
    
    def minus(self, items):
        return "minus "
    
    def leq(self, items):
        return "less than or equal to"
    
    def rho(self, items):
        if items:
            if items[0] == "0":
                return f"rho naught"
            else:
                return f"rho {items[0]}"
        else:
            return f"rho"
    
    def text(self, items):
        return f"{items[0]}"
    
    def less_than(self, items):
        return "less than"
    
    def pi(self, items):
        return f"pi"
    
    def mod(self, items):
        return f"modulus of {items[0]}"
    
    def cdot(self, items):
        return f"into"
    
    def times(self, items):
        return f"times"
    
    def epsilon(self, items):
        if items:
            if items[0] == "0":
                return f"epsilon naught"
            else:
                return f"epsilon {items[0]}"
        else:
            return f"epsilon"
    
    def mu(self, items):
        if items:
            if items[0] == "0":
                return f"mu naught"
            else:
                return f"mu {items[0]}"
        else:
            return f"mu "
        
    def quad(self, items):
        return f"[[slnc 500]] "
    
    def otimes(self, items):
        return f"into the plane of the paper "
    
    def dx(self, items):
        if len(items[0]) == 1:
            return f"d {items[0]} "
        else:
            return f"differential of {items[0]} "
    
    
    def delta(self, items):
        return f"delta"
    
    # def derivative(self, items):
    #     return f"derivative of {items[0]} with respect to {items[1]}"
    
    def x(self, items):
        return f"x"
    
    def sin(self, items):
        return f"sine of {items[0]}"
    
    def cos(self, items):
        return f"cosine of {items[0]}"
    
    def tan(self, items):
        return f"tangent of {items[0]}"
    
    def cot(self, items):
        return f"cotangent of {items[0]}"
    
    def sec(self, items):
        return f"secant of {items[0]}"
    
    def cosec(self, items):
        return f"cosecant of {items[0]}"
    
    def theta(self, items):
        return f"theta"
    
    def integral(self, items):
        if len(items) == 4:
            return f"integral of {items[2]} with respect to {items[3]} from {items[0]} to {items[1]}"
        elif len(items) == 1:
            return f"integral of {items[0]}"
        else:
            return f"integral of {items[0]} with respect to {items[1]}"
        
    
    def circular_integral(self, items):
        return f"circular integral of "
        
    
    def command(self, items):
        return str(items[0])
    
    def DECIMAL(self, items):
        return str(items[0]+items[1]+items[2])
    
    def INTEGER(self, items):
        return str(items[0])
    
    
    
    def milli_ampere(self, items):
        if items:
            return f"{items[0]} milli-ampere "
        else:
            return f"milli-ampere "
    
    def volts(self, items):
        if items:
            return f"{items[0]} volts "
        else:
            return f"volts "
    
    def seconds(self, items):
        if items:
            return f"{items[0]} seconds "
        else:
            return f"seconds "
    
    def speed(self, items):
        if items:
            return f"{items[0]} meters per second "
        else:
            return f"meters per second "
    
    def ohm(self, items):
        if items:
            return f"{items[0]} ohm "
        else:
            return f"ohm "
        
    def meter(self, items):
        if items:
            return f"{items[0]} meter "
        else:
            return f"meter "
        
    def centimeter(self, items):
        return f"centimeter "
    
    def by(self, items):
        return f"by "
    
    def ratio(self, items):
        return f"ratio "
    
    def degree(self, items):
        return f"degrees "
    
    def phi(self, items):
        return f"phi "
    
    
    
        
    def tesla(self, items):
        if items:
            return f"{items[0]} tesla "
        else:
            return f"tesla "
        
    def ampere(self, items):
        if items:
            return f"{items[0]} ampere "
        else:
            return f"ampere "
        
    def newton(self, items):
        if items:
            return f'{"".join(str(item) for item in items)} newton '
        else:
            return f"newton "
        
    def pause(self, items):
        return f"[[slnc {items[0]}]]"
    
    def latex_command(self, items):
    # items[0] is the matched WORD token
        return items[0].value

p = Lark(latex_maths_grammar, parser='lalr', transformer=LaTeXTransformerMaths())
for i in p.terminals:
    print(i)

def parse_and_transform_maths(latex_expression):
    try:
        latex_parser = Lark(latex_maths_grammar, start='start', parser='lalr', lexer='standard')
        transformer = LaTeXTransformerMaths()

        parse_tree = latex_parser.parse(latex_expression)
        # Transform the parse tree into an English representation
        english_representation = transformer.transform(parse_tree)
        print(english_representation)

        return english_representation.children[0].replace(r"-", r"minus ")
    except LarkError as e:
        print(f"An error occurred while parsing or transforming the LaTeX expression: {e}")
        return None



