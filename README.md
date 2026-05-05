# 🧱 SOLID Principles

> The 5 Principles of Clean Object-Oriented Design

SOLID principles help developers write:

- ✅ Clean Code
- ✅ Reusable Components
- ✅ Maintainable Systems
- ✅ Scalable Applications
- ✅ Testable Architecture

---

# 📚 What is SOLID?

| Letter | Principle |
|---|---|
| **S** | Single Responsibility Principle |
| **O** | Open/Closed Principle |
| **L** | Liskov Substitution Principle |
| **I** | Interface Segregation Principle |
| **D** | Dependency Inversion Principle |

---

# 1️⃣ Single Responsibility Principle (SRP)

## 📖 Definition

A class should have **only one reason to change**.

### 💡 Main Idea

One class = One responsibility.

---

## ❌ Bad Example

```ts
class UserService {
  saveUser() {}
  sendEmail() {}
  generateReport() {}
}
```

This class handles multiple responsibilities.

---

## ✅ Good Example

```ts
class UserService {
  saveUser() {}
}

class EmailService {
  sendEmail() {}
}

class ReportService {
  generateReport() {}
}
```

---

## 🎯 Benefits

- Cleaner code
- Easier debugging
- Better maintainability

---

# 2️⃣ Open/Closed Principle (OCP)

## 📖 Definition

Software entities should be:

- Open for extension
- Closed for modification

### 💡 Main Idea

Add new functionality without changing existing code.

---

## ❌ Bad Example

```ts
class PaymentService {
  pay(type: string) {
    if (type === 'card') {
      console.log('Card payment');
    }

    if (type === 'upi') {
      console.log('UPI payment');
    }
  }
}
```

Adding new payment types requires modifying existing logic.

---

## ✅ Good Example

```ts
interface PaymentMethod {
  pay(): void;
}

class CardPayment implements PaymentMethod {
  pay() {
    console.log('Card payment');
  }
}

class UpiPayment implements PaymentMethod {
  pay() {
    console.log('UPI payment');
  }
}
```

---

## 🎯 Benefits

- Flexible architecture
- Easier feature additions
- Reduced risk of breaking existing code

---

# 3️⃣ Liskov Substitution Principle (LSP)

## 📖 Definition

Subclasses should be replaceable for their base classes without altering correctness.

### 💡 Main Idea

Child classes must behave properly like parent classes.

---

## ❌ Bad Example

```ts
class Bird {
  fly() {}
}

class Penguin extends Bird {
  fly() {
    throw new Error("Penguins can't fly");
  }
}
```

Penguin breaks expected behavior.

---

## ✅ Good Example

```ts
class Bird {}

class FlyingBird extends Bird {
  fly() {}
}

class Sparrow extends FlyingBird {}

class Penguin extends Bird {}
```

---

## 🎯 Benefits

- Better inheritance structure
- Safer polymorphism
- Fewer runtime issues

---

# 4️⃣ Interface Segregation Principle (ISP)

## 📖 Definition

Clients should not be forced to depend on methods they do not use.

### 💡 Main Idea

Prefer small and focused interfaces.

---

## ❌ Bad Example

```ts
interface Worker {
  work(): void;
  eat(): void;
}

class Robot implements Worker {
  work() {}

  eat() {
    throw new Error('Robot does not eat');
  }
}
```

Robot is forced to implement unnecessary functionality.

---

## ✅ Good Example

```ts
interface Workable {
  work(): void;
}

interface Eatable {
  eat(): void;
}

class Human implements Workable, Eatable {
  work() {}
  eat() {}
}

class Robot implements Workable {
  work() {}
}
```

---

## 🎯 Benefits

- Cleaner contracts
- Better flexibility
- Easier maintenance

---

# 5️⃣ Dependency Inversion Principle (DIP)

## 📖 Definition

Depend on abstractions, not concrete implementations.

### 💡 Main Idea

High-level modules should not depend directly on low-level modules.

---

## ❌ Bad Example

```ts
class MySQLDatabase {
  connect() {}
}

class UserRepository {
  private db = new MySQLDatabase();
}
```

Repository is tightly coupled to MySQL.

---

## ✅ Good Example

```ts
interface Database {
  connect(): void;
}

class MySQLDatabase implements Database {
  connect() {}
}

class MongoDatabase implements Database {
  connect() {}
}

class UserRepository {
  constructor(private db: Database) {}
}
```

---

## 🎯 Benefits

- Loose coupling
- Easier testing
- Flexible implementation changes

---

# 🧠 Easy Memory Trick

| Principle | Simple Meaning |
|---|---|
| **S** | One job |
| **O** | Extend without changing |
| **L** | Safe replacement |
| **I** | Small interfaces |
| **D** | Depend on abstractions |

---

# 🚀 Why SOLID Matters

Without SOLID:

- ❌ Messy code
- ❌ Tight coupling
- ❌ Difficult testing
- ❌ Hard maintenance

With SOLID:

- ✅ Clean architecture
- ✅ Reusable code
- ✅ Scalable systems
- ✅ Easier debugging
- ✅ Enterprise-ready applications

---

# 🛠 Commonly Used In

- Angular
- React
- NestJS
- Java Spring Boot
- .NET Applications
- Enterprise Software

---

# 📌 Final Summary

SOLID principles are the foundation of professional software architecture.

They help developers build:

- ✅ Maintainable Applications
- ✅ Flexible Systems
- ✅ Reusable Components
- ✅ Scalable Projects
- ✅ Clean Enterprise Code

---

# ⭐ If You Found This Helpful

Give this repository a ⭐ on GitHub and keep learning clean architecture 🚀