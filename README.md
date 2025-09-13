# LeetCode Test Solutions

This repository contains solutions to various LeetCode problems implemented in both TypeScript and Python.

## 📁 Project Structure

```
leetcode-tests/
├── javascript/          # TypeScript implementations
│   ├── duplicate_integer/
│   ├── top_k_elements_list/
│   ├── two_integer_sum/
│   ├── valid_anagram/
│   ├── package.json
│   ├── package-lock.json
│   └── tsconfig.json
├── python/              # Python implementations
│   ├── duplicate_integer/
│   ├── top_k_elements_list/
│   ├── two_integer_sum/
│   └── valid_anagram/
└── README.md
```

## 🚀 Getting Started

### TypeScript Setup

1. **Navigate to the JavaScript directory:**

   ```bash
   cd javascript
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

### Running TypeScript Files

You have several options to run the TypeScript implementations:

#### Option 1: Using ts-node (Recommended)

```bash
# Run individual files
npx ts-node duplicate_integer/index.ts
npx ts-node top_k_elements_list/index.ts
npx ts-node two_integer_sum/index.ts
npx ts-node valid_anagram/index.ts
```

#### Option 2: Compile then Run

```bash
# Compile all TypeScript files
npm run build

# Run the compiled JavaScript files
node duplicate_integer/index.js
node top_k_elements_list/index.js
node two_integer_sum/index.js
node valid_anagram/index.js
```

#### Option 3: Global ts-node (One-time setup)

```bash
# Install ts-node globally
npm install -g ts-node

# Then run directly
ts-node duplicate_integer/index.ts
```

### Running Python Files

Python files can be run directly without any additional setup:

```bash
# Navigate to the python directory
cd python

# Run individual files
python duplicate_integer/index.py
python top_k_elements_list/index.py
python two_integer_sum/index.py
python valid_anagram/index.py
```

## 📋 Problem Descriptions

### 1. Duplicate Integer

**File:** `duplicate_integer/index.*`

- **Problem:** Given an integer array, return `true` if any value appears more than once.
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

### 2. Top K Elements

**File:** `top_k_elements_list/index.*`

- **Problem:** Given an integer array and an integer k, return the k most frequent elements.
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

### 3. Two Integer Sum

**File:** `two_integer_sum/index.*`

- **Problem:** Given an array of integers and a target, return indices of two numbers that add up to the target.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

### 4. Valid Anagram

**File:** `valid_anagram/index.*`

- **Problem:** Given two strings, return `true` if they are anagrams of each other.
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

## 🛠️ Development

### TypeScript Configuration

The project uses the following TypeScript configuration:

- **Target:** ES2020
- **Module:** CommonJS
- **Module Resolution:** Bundler
- **Strict mode:** Enabled

### Dependencies

- **TypeScript:** ^5.1.6
- **ts-node:** ^10.9.1
- **@types/node:** ^20.5.0

## 📝 Example Usage

### TypeScript Example

```bash
cd javascript
npx ts-node duplicate_integer/index.ts
```

### Python Example

```bash
cd python
python duplicate_integer/index.py
```

Both implementations will run their respective test cases and display the results in the console.
# leetcode-test
