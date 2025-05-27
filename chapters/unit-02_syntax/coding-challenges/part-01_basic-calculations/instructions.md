# **Part 1: Basic Calculations - Your First Python Engineering Application**

## **🎯 Project Overview**

You've learned the fundamental building blocks of Python in **Chapter 2** *(or you just skipped straight to this coding challenge, which is also fine!)*. Now it's time to put those concepts together to build something real: a *stress and strain calculator* that actual engineers use in the field. This is the first part of a **6-part journey** of coding challenges where you'll build the same application using increasingly sophisticated Python techniques.

This calculator will grow with your Python skills. In **Part 1**, you'll use *basic calculations* with *variables* and *operators*. Later parts will add input validation, data organization, functions, object-oriented design, and finally a complete modular application.

## **🔧 Why This Project Matters**

Stress and strain analysis is fundamental to **all structural engineering**. Civil engineers use it to design bridges and buildings, mechanical engineers apply it to machine components, and aerospace engineers rely on it for aircraft structures. By building this calculator, you're creating a tool that has *real professional value* while mastering Python syntax.

*And yes, this is the kind of thing you might actually use in your engineering career - we're not building another "guess the number" game here!*

## **📚 Engineering Background**

Think of stretching a rubber band *(you've probably done this a thousand times)*. **Stress** measures how much force you're applying per unit area, calculated as *force divided by area* (`σ = F/A`) and measured in *Pascals*. **Strain** measures how much the material deforms relative to its original size, calculated as the *change in length divided by original length* (`ε = ΔL/L₀`). Strain is *dimensionless* because it's a ratio.

For example, imagine a **steel cable in a bridge** with an original length of 10 meters. If you apply 50,000 N of force to a cable with 0.01 m² cross-section and it stretches by 5 mm, your calculator would find a stress of **5,000,000 Pa** and a strain of **0.0005**. Engineers use these values to ensure the cable won't break, *which is pretty important when people are driving over it!*

## **🎓 Learning Objectives**

This challenge directly applies everything from **Chapter 2**. You'll combine *multiple Python concepts* in a single program and learn to translate engineering formulas into working code. More importantly, you'll develop problem-solving skills that apply *far beyond* this specific calculator.

**Chapter 2 concepts you'll use:**
- *Variables* and *data types* for storing engineering parameters
- *Arithmetic operators* for performing calculations  
- *Type conversion* to handle user input
- *String formatting* to display professional results
- *Input/output* for user interaction

*Notice how we're not using these concepts in isolation anymore - this is where the real learning happens!*

## **📋 Requirements**

Your program should collect **four engineering parameters** from the user:
- Applied force *(in Newtons)*
- Cross-sectional area *(in square meters)*
- Original length *(in meters)*
- Change in length *(in meters)*

Use the `input()` function to collect these values and convert them to *floats* for calculations *(because engineers work with decimal numbers, not just integers)*. Implement the two fundamental engineering formulas: **stress equals force divided by area**, and **strain equals change in length divided by original length**.

Display both the input values and calculated results with *proper formatting*. Use **f-strings** to format stress with 2 decimal places and strain with 6 decimal places, since strain values are typically *very small*. Your output should look **professional** and include proper units. Remember that strain is *dimensionless*, so it doesn't need units. *It's just a ratio, after all*.

## **🧪 Test Your Program**

Use these **realistic engineering values** to verify your calculator works correctly *(trust us, these numbers come from real engineering scenarios)*:

**Test Case 1: Steel Cable**
- Force: 50,000 N, Area: 0.01 m², Original Length: 10 m, Change: 0.005 m
- **Expected:** Stress = 5,000,000 Pa, Strain = 0.0005

**Test Case 2: Aluminum Bar**  
- Force: 10,000 N, Area: 0.002 m², Original Length: 1 m, Change: 0.0015 m
- **Expected:** Stress = 5,000,000 Pa, Strain = 0.0015

*(If your results don't match these expected values, double-check your formulas - the math doesn't lie!)*

## **🚀 Getting Started**

Start with the provided `template.py` file and follow the **TODO comments** as your guide *(they're there to help, not to annoy you)*. The template provides the basic structure and helps you focus on implementing the *core concepts* rather than figuring out the overall program flow. You can compare your completed work to `solution.py`.

You don't have to use the provided template if you are confident enough. You can also just solve this task using a new `.py` file

Focus on writing **clear, commented code** that others can understand. *Including your future self when you look at this code in six months*. Use *meaningful variable names* that reflect engineering terminology, and organize your code logically with proper program structure.

## **🏆 Success Criteria**

Your program is successful when it:
- Accepts all four inputs *without errors*
- Performs calculations correctly *(verify with test cases)*
- Displays results with *proper formatting and units*
- Uses *meaningful variable names* and comments

*Don't worry about input validation yet - we'll tackle that in **Part 2**. For now, assume users will enter valid numbers.*

## **🎯 Extension Ideas (Optional)**

If you finish early and want to explore further *(always a good sign of a curious programmer!)*:
- Convert stress to different units *(kPa, MPa)*
- Determine if loading is *tension* (positive) or *compression* (negative)
- Calculate the *stress-to-strain ratio* (that's Young's modulus!)

## **🔮 Looking Ahead**

This basic calculator is just the **beginning**. In future parts, you'll add material selection and input validation, create material databases and test result storage, implement modular functions, design object-oriented material classes, and finally build a complete professional application. Each part will build on this foundation, showing you how *professional Python applications* evolve from simple scripts to sophisticated tools.

*Spoiler alert: by Part 6, you'll have built something that looks much more like actual engineering software!*

---

**Ready to code?** Start with `template.py` and let's build something using Python! 🚀🐍