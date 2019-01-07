package net.sf.jclec.exprtree;

import java.util.Arrays;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Comparator;

import net.sf.jclec.JCLEC;

import net.sf.jclec.util.random.IRandGen;

import org.apache.commons.lang.builder.EqualsBuilder;

/**
 * Structural information about ExprTrees.
 * 
 * @author Sebastian Ventura 
 */

public class ExprTreeSchema implements JCLEC
{
	/////////////////////////////////////////////////////////////
	// ----------------------------------- Serialization constant
	/////////////////////////////////////////////////////////////

	/** Generated by Eclipse */
	
	private static final long serialVersionUID = -2204221331549325549L;

	/////////////////////////////////////////////////////////////
	// ----------------------------------------------- Attributes
	/////////////////////////////////////////////////////////////

	/** Minimum tree size */
	
	protected int minTreeSize;

	/** Maximum tree size */
	
	protected int maxTreeSize;
	
	/** Root type */
	
	protected Class<?> rootType;
	
	/** Terminal blocks */
	
	protected IPrimitive [] terminals;
	
	/** Function blocks */
	
	protected IPrimitive [] functions;
	
	/////////////////////////////////////////////////////////////
	// --------------------------------------- Internal variables
	/////////////////////////////////////////////////////////////
	
	/** All blocks map */
	
	protected HashMap<Class<?>, IPrimitive[]> allMap;
	
	/** Terminal blocks map */
	
	protected HashMap<Class<?>, IPrimitive[]> termMap;
	
	/** Function blocks map */
	
	protected HashMap<Class<?>, IPrimitive[]> funcMap;
	
	/////////////////////////////////////////////////////////////
	// ------------------------------------------- Public methods
	/////////////////////////////////////////////////////////////		
	
	// Set properties
	
	/**
	 * @return the terminals
	 */
	public IPrimitive[] getTerminals() {
		return terminals;
	}

	/**
	 * @return the functions
	 */
	public IPrimitive[] getFunctions() {
		return functions;
	}
	
	/**
	 * Sets the root type for the expression trees represented by
	 * this schema
	 * 
	 * @param rootType Root type
	 */
	
	public final void setRootType(Class<?> rootType) 
	{
		this.rootType = rootType;
	}

	/**
	 * Sets the minimum size for the expression trees represented 
	 * by this schema
	 * 
	 * @param minTreeSize Minimum tree size
	 */

	public final void setMinTreeSize(int minTreeSize) 
	{
		this.minTreeSize = minTreeSize;
	}

	/**
	 * Sets the maximum size for the expression trees represented 
	 * by this schema
	 * 
	 * @param maxTreeSize Minimum tree size
	 */

	public final void setMaxTreeSize(int maxTreeSize) 
	{
		this.maxTreeSize = maxTreeSize;
	}

	/**
	 * Set the terminals that can be used to build valid expression 
	 * trees.
	 * 
	 * @param terminals Valid terminal nodes
	 */
	
	public final void setTerminals(IPrimitive[] terminals) 
	{
		// Set terminals
		this.terminals = terminals;
		// If functions was previously set... create maps
		if (functions != null) generateBlockMaps();
	}

	/**
	 * Set the functions that can be used to build valid expression 
	 * trees.
	 * 
	 * @param functions Valid function nodes
	 */
	
	public void setFunctions(IPrimitive[] functions) 
	{
		this.functions = functions;
		// If terminals was previously set... create maps
		if (terminals != null) generateBlockMaps();
	}
	
	// IExpTreeSchema interface
	
	/**
	 * Informs about the return (root) type for this expression.
	 * 
	 * @return Root (return) type
	 */
	
	public Class<?> getRootType() 
	{
		return rootType;
	}

	/** Minimum tree size */
	
	public int getMinTreeSize()
	{
		return minTreeSize;
	}
	
	/** Maximum tree size */
	
	public int getMaxTreeSize()
	{
		return maxTreeSize;
	}
	
	/**
	 * Informs about the number of possible functions.
	 * 
	 * @return Number of function blocks
	 */
	
	public int getNumFunctionBlocks(Class<?> rtype)
	{
		return funcMap.get(rtype).length;
	}
	
	/**
	 * Choose a valid terminal block (used in full methods).
	 * 
	 * @param rtype   Return type for the block
	 * 
	 * @return A valid block for this tree
	 */
	
	public IPrimitive getTerminalBlock(Class<?> rtype, IRandGen randgen) 
	{
		// Gets desired terminals list
		IPrimitive [] termBlocks = termMap.get(rtype);
		// Randomly choose the block
		IPrimitive result = termBlocks[randgen.choose(0, termBlocks.length)];
		return result.instance(); 
	}

	/**
	 * Choose a valid function block.
	 * 
	 * @param rtype   Return type for the block
	 * @param randgen Random generator used
	 * 
	 * @return A valid block for this tree
	 */

	public IPrimitive getFunctionBlock(Class<?> rtype, IRandGen randgen) 
	{
		IPrimitive result;
		// Gets desired functions list
		IPrimitive [] funcBlocks = funcMap.get(rtype);		
		// Choose function at random
		result = funcBlocks[randgen.choose(0, funcBlocks.length)]; 
		// Return result
		return result.instance();
	}

	/**
	 * Choose a valid function block (with given arity).
	 * 
	 * @param rtype   Return type for the block
	 * @param randgen Random generator used
	 * @param arity   Block arity
	 * 
	 * @return A valid block for this tree
	 */

	public IPrimitive getFunctionBlock(Class<?> rtype, IRandGen randgen, int arity) {
		IPrimitive result;
		// Gets desired functions list
		IPrimitive [] funcBlocks = funcMap.get(rtype);
		// Choose function at random
		do {
			result = funcBlocks[randgen.choose(0, funcBlocks.length)];
		}
		while(result.argumentTypes().length != arity);
		// Return result
		return result.instance();
	}

	/**
	 * Choose a valid function block (with given arity).
	 * 
	 * @param rtype    Return type for the block
	 * @param randgen  Random generator used
	 * @param minArity Minimum arity
	 * @param maxArity Maximum arity
	 * 
	 * @return A valid block for this tree
	 */

	public IPrimitive getFunctionBlockBetweenMinMaxArity(Class<?> rtype, IRandGen randgen, int minArity, int maxArity) {
		
		//Gets desired functions list
		IPrimitive [] funcBlocks = funcMap.get(rtype);
		// Set initial and final indexes
		int initialIndex = 0;
		int finalIndex = 0;
		for (;finalIndex < funcBlocks.length;) {
			// Choose function at random
			if (funcBlocks[finalIndex].argumentTypes().length < minArity) {
				initialIndex++;
			}
			if (funcBlocks[finalIndex].argumentTypes().length > maxArity) {
				break;
			}
			finalIndex++;
		}
		if (finalIndex == 0) {
			return null;				
		}
		else {
			return funcBlocks[randgen.choose(initialIndex, finalIndex)];				
		}
	}

	/**
	 * Choose a valid block.
	 * 
	 * @param rtype   Return type for the block
	 * @param randgen Random generator used
	 * 
	 * @return A valid function with arity from minArity to maxArity
	 */

	public IPrimitive getAnyBlock(Class<?> rtype, IRandGen randgen) 
	{
		IPrimitive result;
		// Gets desired functions list
		IPrimitive [] allBlocks = allMap.get(rtype);		
		// Choose a block at random
		result = allBlocks[randgen.choose(0, allBlocks.length)];
		// Return result
		return result.instance();
	}

	/**
	 * Choose a valid block  (with given arity).
	 * 
	 * @param rtype   Return type for the block
	 * @param randgen Random generator used
	 * @param arity   Block arity
	 * 
	 * @return A valid block for this tree
	 */

	public IPrimitive getAnyBlock(Class<?> rtype, IRandGen randgen, int arity) 
	{
		IPrimitive result;
		// Gets desired functions list
		IPrimitive [] allBlocks = allMap.get(rtype);		
		// Choose  a block at random
		do {
			result = allBlocks[randgen.choose(0, allBlocks.length)];
		}
		while(result.argumentTypes().length != arity);
		// Return result
		return result.instance();
	}

	/**
	 * Expression tree creation.
	 * 
	 * @param maxSize Maximum tree size
	 * @param randgen Random generator
	 * 
	 * @return A new expression tree object...
	 */
	
	public ExprTree createExprTree(int maxSize, IRandGen randgen) 
	{
		// Create resulting expression
		ExprTree result = new ExprTree();
		// Fill resultig expression
		fillExprBranch(result, rootType, maxSize, randgen);
		// Return result
		return result;
	}

	/**
	 * Create a brach randomly, putting it in the expression tree passed as argument.
	 * 
	 * @param exprTree  Tree that contains this branch
	 * @param returnType Return type for this branch
	 * @param maxSize    Brach size 
	 * @param randgen    Random generator used
	 */
	
	public void fillExprBranch(ExprTree exprTree, Class<?> returnType, int maxSize, IRandGen randgen) 
	{
		// Root node
		IPrimitive root;
		// Select root node
		if (maxSize == 1) {
			root = getTerminalBlock(returnType, randgen);
		}
		else {
			root = getBranchBlock(returnType, randgen, maxSize-1);
		}
		// Add root node to the expression
		exprTree.addBlock(root);
		// Sons types
		Class<?> [] sonTypes = root.argumentTypes();
		// Number of sons
		int numberOfSons = sonTypes.length;
		// Call recursively fillBranch (if necessary)
		if (numberOfSons != 0) {
			// Assign maximum subbrach size
			int newMaxSize = (maxSize-1)/numberOfSons;
			// Security mechanism (ensures maxSize >= 1)
			if (newMaxSize<1) newMaxSize = 1;
			// Call fillBranch recursively
			for (int i=0; i<numberOfSons; i++) {
				fillExprBranch(exprTree, sonTypes[i], newMaxSize, randgen);
			}
		}
	}

	// java.lang.Object methods
	
	/**
	 * {@inheritDoc}
	 */
	
	public boolean equals(Object other)
	{
		if (other instanceof ExprTreeSchema) {
			ExprTreeSchema cother = (ExprTreeSchema) other;
			EqualsBuilder eb = new EqualsBuilder();
			eb.append(minTreeSize, cother.minTreeSize);
			eb.append(maxTreeSize, cother.maxTreeSize);
			eb.append(rootType, cother.rootType);
			eb.append(functions, cother.functions);
			eb.append(terminals, cother.terminals);
			return eb.isEquals();
		}
		else {
			return false;
		}
	}

	/////////////////////////////////////////////////////////////
	// ---------------------------------------- Protected methods
	/////////////////////////////////////////////////////////////
	
	/**
	 * Generate block maps. This method must be invoked after set 
	 * terminal and  function blocks  and before  call  any block 
	 * provision method.
	 */
	
	protected final void generateBlockMaps()
	{
		// Used to sort primitives by arity
		Comparator<IPrimitive> arityComparator = new Comparator<IPrimitive>() 
		{
			public int compare(IPrimitive one, IPrimitive two) 
			{
				int onearity = one.argumentTypes().length;
				int twoarity = two.argumentTypes().length;
				if (onearity > twoarity) {
					return 1;
				}
				if (onearity < twoarity) {
					return -1;
				}
				return 0;
			}				
		};
		// Temporary maps (store all classified blocks)
		HashMap<Class<?>, ArrayList<IPrimitive>> allMapTmp = 
			new HashMap<Class<?>, ArrayList<IPrimitive>>();
		HashMap<Class<?>, ArrayList<IPrimitive>> termMapTmp =
			new HashMap<Class<?>, ArrayList<IPrimitive>>();
		HashMap<Class<?>, ArrayList<IPrimitive>> funcMapTmp = 
			new HashMap<Class<?>, ArrayList<IPrimitive>>();
		// Classify terminal blocks
		for (IPrimitive block : terminals) {
			// Return type
			Class<?> returnType = block.returnType();
			// Register this block in allMapTmp and in termMapTmp
			if (! allMapTmp.containsKey(returnType) ) {
				allMapTmp.put(returnType, new ArrayList<IPrimitive>());
				termMapTmp.put(returnType, new ArrayList<IPrimitive>());
			}
			// Register in allMapTmp
			allMapTmp.get(returnType).add(block);
			// Register in termMapTmp
			termMapTmp.get(returnType).add(block);
		}
		// Classify function blocks
		for (IPrimitive block : functions) {
			// Return type
			Class<?> returnType = block.returnType();
			// Register this block in allMapTmp
			if (! allMapTmp.containsKey(returnType) ) {
				allMapTmp.put(returnType, new ArrayList<IPrimitive>());
			}
			allMapTmp.get(returnType).add(block);
			// Register this block in funcMapTmp
			if (! funcMapTmp.containsKey(returnType) ) {
				funcMapTmp.put(returnType, new ArrayList<IPrimitive>());					
			}
			funcMapTmp.get(returnType).add(block);
		}
		// Create allMap 
		allMap = new HashMap<Class<?>, IPrimitive[]> ();
		for (Class<?> key : allMapTmp.keySet()) {
			// Convert blocks list to array 
			IPrimitive [] aux = 
				allMapTmp.get(key).toArray(new IPrimitive [0]);
			// Sort array elements by arity
			Arrays.sort(aux, arityComparator);
			// Put array in allMap
			allMap.put(key, aux);
		}
		// Create termMap
		termMap = new HashMap<Class<?>, IPrimitive[]> ();
		for (Class<?> key : termMapTmp.keySet()) {
			// Convert blocks list to array 
			IPrimitive [] aux = 
				termMapTmp.get(key).toArray(new IPrimitive[0]);
			// Sort array elements by arity
			Arrays.sort(aux, arityComparator);
			// Put array in termMap
			termMap.put(key, aux);
		}
		// Create funcMap
		funcMap = new HashMap<Class<?>, IPrimitive[]> ();
		for (Class<?> key : funcMapTmp.keySet()) {
			// Convert blocks list to array 
			IPrimitive [] aux = 
				funcMapTmp.get(key).toArray(new IPrimitive[0]);
			// Sort array elements by arity
			Arrays.sort(aux, arityComparator);
			// Put array in termMap
			funcMap.put(key, aux);
		}
	}

	protected final IPrimitive getBranchBlock(Class<?> returnType, IRandGen randgen, int arity)
	{
		// Gets desired functions list
		IPrimitive [] funcBlocks = funcMap.get(returnType);
		// Set initial and final indexes
		int auxIndex = 0;
		for (;funcBlocks != null && auxIndex < funcBlocks.length;) {
			// Choose function at random
			if (funcBlocks[auxIndex].argumentTypes().length > arity) {
				break;
			}
			auxIndex++;
		}
		if (auxIndex == 0) {
			return getTerminalBlock(returnType, randgen);				
		}
		else {
			return funcBlocks[randgen.choose(0, auxIndex)];				
		}
	}
}