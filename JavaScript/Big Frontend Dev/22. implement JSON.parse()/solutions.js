/**
 * Hardened, production-grade JSON parser using sequential look-ahead recursive descent.
 * Safeguarded against prototype pollution, whitespace variations, and primitive falsy short-circuits.
 * * @param {string} str - The raw serialized JSON string sequence to parse
 * @returns {*} The parsed primitive value or object graph mapping
 * @throws {SyntaxError} For structural grammar violations or unconsumed trailing tokens
 */
function parse(str) {
  let i = 0;
  
  // Advance to initial semantic start block
  skipWhitespace();
  
  if (str.length === 0) {
    throw new SyntaxError('JSON Constraint Violation: Cannot parse an empty string.');
  }

  const result = parseValue();
  
  // Verify trailing spacing and check for trailing anomalies
  skipWhitespace();
  if (i < str.length) {
    throw new SyntaxError(`SyntaxError: Unexpected trailing data tokens past root entity at index ${i}`);
  }
  
  return result;

  /**
   * Advances the global state cursor past all formatting and non-semantic characters.
   */
  function skipWhitespace() {
    while (i < str.length && (str[i] === ' ' || str[i] === '\n' || str[i] === '\r' || str[i] === '\t')) {
      i += 1;
    }
  }

  /**
   * Evaluation switchboard tracking input types dynamically via look-ahead characters.
   */
  function parseValue() {
    skipWhitespace();
    
    if (i >= str.length) {
      throw new SyntaxError('SyntaxError: Unexpected termination of JSON input stream inside value parser.');
    }

    const char = str[i];
    
    // Explicit Type Routing
    if (char === '"') return parseString();
    if (char === '{') return parseObject();
    if (char === '[') return parseArray();
    if (char === '-' || (char >= '0' && char <= '9')) return parseNumber();
    
    // Process literal primitives securely via exact text sequence validation
    const literalKeyword = parseKeywords();
    if (literalKeyword !== undefined) return literalKeyword;

    throw new SyntaxError(`SyntaxError: Invalid token element definition "${char}" encountered at index ${i}`);
  }

  /**
   * Scans and verifies mathematical floating point, negative, or exponential literals.
   */
  function parseNumber() {
    const start = i;
    
    if (str[i] === '-') i += 1;
    
    // Advance across standard integer, numeric float, and scientific exponential characters
    while (i < str.length && /[0-9.\-eE+]/.test(str[i])) {
      i += 1;
    }
    
    const tokenStr = str.slice(start, i);
    const numericValue = Number(tokenStr);
    
    if (Number.isNaN(numericValue) || tokenStr === '') {
      throw new SyntaxError(`SyntaxError: Invalid numeric token parsing allocation: "${tokenStr}" at index ${start}`);
    }
    return numericValue;
  }

  /**
   * Extracts double-quoted string literals while safely stepping past escape boundaries.
   */
  function parseString() {
    if (str[i] === '"') {
      let accumulatedString = '';
      i += 1; // Step past opening quote string marker
      
      while (i < str.length && str[i] !== '"') {
        if (str[i] === '\\') {
          i += 1;
          if (i >= str.length) throw new SyntaxError('SyntaxError: Unterminated string escape block.');
        }
        accumulatedString += str[i];
        i += 1;
      }
      
      if (str[i] !== '"') {
        throw new SyntaxError('SyntaxError: Unterminated string boundary segment detected.');
      }
      i += 1; // Step past trailing closing quote marker
      return accumulatedString;
    }
  }

  /**
   * Synthesizes structural object structures using zero-prototype containers to prevent injection bugs.
   */
  function parseObject() {
    if (str[i] === '{') {
      i += 1;
      
      // Hardening Shield: Object prototype completely stripped to prevent prototype pollution exploits
      const objectMap = Object.create(null);
      let isInitialIteration = true;
      
      skipWhitespace();
      if (str[i] === '}') {
        i += 1;
        return objectMap;
      }

      while (i < str.length && str[i] !== '}') {
        if (!isInitialIteration) {
          consumePunctuation(',');
        }
        
        skipWhitespace();
        const propertyKey = parseString();
        if (propertyKey === undefined) {
          throw new SyntaxError(`SyntaxError: Expected valid string declaration for object dictionary key at index ${i}`);
        }
        
        // Security Assertion Guard
        if (propertyKey === '__proto__' || propertyKey === 'constructor') {
          throw new SecurityError(`Security Exception: Terminating compilation pass. Prototype modification blocked for key: "${propertyKey}"`);
        }

        consumePunctuation(':');
        
        const propertyValue = parseValue();
        objectMap[propertyKey] = propertyValue;
        
        isInitialIteration = false;
        skipWhitespace();
      }
      
      if (str[i] !== '}') {
        throw new SyntaxError(`SyntaxError: Object literal container missing closing bracket sequence at index ${i}`);
      }
      i += 1; // Advance past trailing close bracket
      return objectMap;
    }
  }

  /**
   * Constructs list configurations sequentially, enforcing recursive item unwrapping.
   */
  function parseArray() {
    if (str[i] === '[') {
      i += 1;
      const arrayList = [];
      let isInitialIteration = true;
      
      skipWhitespace();
      if (str[i] === ']') {
        i += 1;
        return arrayList;
      }

      while (i < str.length && str[i] !== ']') {
        if (!isInitialIteration) {
          consumePunctuation(',');
        }
        
        const elementValue = parseValue();
        arrayList.push(elementValue);
        
        isInitialIteration = false;
        skipWhitespace();
      }
      
      if (str[i] !== ']') {
        throw new SyntaxError(`SyntaxError: Array layout definition missing trailing square bracket closer at index ${i}`);
      }
      i += 1; // Advance past trailing bracket
      return arrayList;
    }
  }

  /**
   * Evaluates literal markers, avoiding nullish operator leaks.
   */
  function parseKeywords() {
    if (str.startsWith('true', i)) { i += 4; return true; }
    if (str.startsWith('false', i)) { i += 5; return false; }
    if (str.startsWith('null', i)) { i += 4; return null; }
    return undefined;
  }

  /**
   * Helper utility to enforce strict structural punctuation formatting.
   */
  function consumePunctuation(expectedToken) {
    skipWhitespace();
    if (str[i] !== expectedToken) {
      throw new SyntaxError(`SyntaxError: Expected structural separation character "${expectedToken}", received "${str[i]}" at index ${i}`);
    }
    i += 1;
  }
}