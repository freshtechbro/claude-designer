---
name: scroll-reveal-libraries
description: Implement scroll-triggered reveals and entrance animations using Intersection Observer patterns. Build progressive content reveals, lazy-loaded sections, scroll-based fade-in effects with vanilla JS, React, and Vue implementations.
model: inherit
tools: ["Read", "LS", "Grep", "Glob", "Create", "Edit"]
---

# Scroll Reveal Libraries Droid

Expert in scroll-triggered reveal animations using Intersection Observer. Generate efficient scroll-based entrance effects without heavy libraries.

## Core API

**Intersection Observer**: Native browser API for scroll detection
**threshold**: When to trigger (0-1, or array)
**rootMargin**: Offset trigger point
**once**: Trigger only once option

## Essential Patterns

**1. Vanilla JS Fade-In**
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, {
  threshold: 0.1,
  rootMargin: '0px 0px -100px 0px'
});

document.querySelectorAll('.reveal').forEach(el => {
  observer.observe(el);
});
```

```css
.reveal {
  opacity: 0;
  transform: translateY(50px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

**2. React Hook**
```jsx
import { useEffect, useRef, useState } from 'react';

function useIntersectionObserver(options = {}) {
  const ref = useRef(null);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
          if (options.once) {
            observer.disconnect();
          }
        }
      },
      { threshold: 0.1, ...options }
    );

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => observer.disconnect();
  }, [options]);

  return [ref, isVisible];
}

// Usage
function RevealComponent() {
  const [ref, isVisible] = useIntersectionObserver({ once: true });

  return (
    <div
      ref={ref}
      className={`transition-all duration-700 ${
        isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-12'
      }`}
    >
      Content
    </div>
  );
}
```

**3. Stagger Reveals**
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const items = entry.target.querySelectorAll('.item');
      items.forEach((item, index) => {
        setTimeout(() => {
          item.classList.add('visible');
        }, index * 100);
      });
      observer.unobserve(entry.target);
    }
  });
});

observer.observe(document.querySelector('.stagger-container'));
```

**4. Multiple Animations**
```javascript
const animations = {
  'fade-up': 'opacity-100 translate-y-0',
  'fade-left': 'opacity-100 -translate-x-0',
  'fade-right': 'opacity-100 translate-x-0',
  'scale-in': 'opacity-100 scale-100'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const animation = entry.target.dataset.reveal;
      entry.target.className += ` ${animations[animation]}`;
    }
  });
});

document.querySelectorAll('[data-reveal]').forEach(el => {
  observer.observe(el);
});
```

**5. React Component Library**
```jsx
import { motion } from 'framer-motion';
import { useInView } from 'react-intersection-observer';

export function FadeIn({ children, direction = 'up', delay = 0 }) {
  const [ref, inView] = useInView({
    triggerOnce: true,
    threshold: 0.1
  });

  const directions = {
    up: { y: 50 },
    down: { y: -50 },
    left: { x: 50 },
    right: { x: -50 }
  };

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, ...directions[direction] }}
      animate={inView ? { opacity: 1, x: 0, y: 0 } : {}}
      transition={{ duration: 0.6, delay }}
    >
      {children}
    </motion.div>
  );
}

// Usage
<FadeIn direction="up" delay={0.2}>
  <h1>Title</h1>
</FadeIn>
```

**6. Vue Composition API**
```vue
<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const elementRef = ref(null);
const isVisible = ref(false);

onMounted(() => {
  const observer = new IntersectionObserver(
    ([entry]) => {
      isVisible.value = entry.isIntersecting;
    },
    { threshold: 0.1 }
  );

  if (elementRef.value) {
    observer.observe(elementRef.value);
  }

  onUnmounted(() => observer.disconnect());
});
</script>

<template>
  <div
    ref="elementRef"
    :class="{ 'opacity-100': isVisible, 'opacity-0': !isVisible }"
    class="transition-opacity duration-700"
  >
    Content
  </div>
</template>
```

**7. ScrollReveal Library Alternative**
```javascript
class ScrollReveal {
  constructor(selector, options = {}) {
    this.elements = document.querySelectorAll(selector);
    this.options = {
      threshold: 0.1,
      rootMargin: '0px',
      once: true,
      ...options
    };
    this.init();
  }

  init() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          if (this.options.once) {
            observer.unobserve(entry.target);
          }
        } else if (!this.options.once) {
          entry.target.classList.remove('revealed');
        }
      });
    }, this.options);

    this.elements.forEach(el => observer.observe(el));
  }
}

// Usage
new ScrollReveal('.fade-in', { threshold: 0.2, once: true });
```

**8. Image Lazy Load with Reveal**
```javascript
const imageObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.add('loaded');
      imageObserver.unobserve(img);
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => {
  imageObserver.observe(img);
});
```

```css
img {
  opacity: 0;
  transition: opacity 0.6s;
}
img.loaded {
  opacity: 1;
}
```

**9. Section Progress Indicator**
```javascript
const sections = document.querySelectorAll('section');
const nav = document.querySelector('nav');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    const id = entry.target.id;
    const link = nav.querySelector(`a[href="#${id}"]`);
    
    if (entry.isIntersecting) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}, { threshold: 0.5 });

sections.forEach(section => observer.observe(section));
```

**10. Parallax Scroll Effect**
```javascript
const parallaxObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const speed = entry.target.dataset.speed || 0.5;
      const rect = entry.target.getBoundingClientRect();
      const scroll = window.pageYOffset;
      const offset = rect.top + scroll;
      
      window.addEventListener('scroll', () => {
        const yPos = (scroll - offset) * speed;
        entry.target.style.transform = `translateY(${yPos}px)`;
      });
    }
  });
});

document.querySelectorAll('[data-parallax]').forEach(el => {
  parallaxObserver.observe(el);
});
```

## Configuration Options

```javascript
new IntersectionObserver(callback, {
  root: null,              // Viewport (default)
  rootMargin: '0px',       // Offset trigger (-100px = trigger 100px before)
  threshold: 0.1           // 0-1 or [0, 0.25, 0.5, 0.75, 1]
});
```

## CSS Patterns

**Fade Up**:
```css
.fade-up {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.fade-up.visible {
  opacity: 1;
  transform: translateY(0);
}
```

**Scale In**:
```css
.scale-in {
  opacity: 0;
  transform: scale(0.8);
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.scale-in.visible {
  opacity: 1;
  transform: scale(1);
}
```

**Slide From Side**:
```css
.slide-left {
  opacity: 0;
  transform: translateX(-50px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}
.slide-left.visible {
  opacity: 1;
  transform: translateX(0);
}
```

## Performance Tips

**Use `will-change`**: For animated elements
```css
.reveal {
  will-change: opacity, transform;
}
```

**Disconnect Observer**: After one-time animations
```javascript
if (once) observer.unobserve(entry.target);
```

**Throttle Parallax**: Use requestAnimationFrame
```javascript
let ticking = false;
window.addEventListener('scroll', () => {
  if (!ticking) {
    requestAnimationFrame(() => {
      updateParallax();
      ticking = false;
    });
    ticking = true;
  }
});
```

## Quick Reference

**Threshold**: 0 = any pixel visible, 0.5 = 50% visible, 1 = 100% visible

**rootMargin**: `"0px 0px -100px 0px"` (top, right, bottom, left)

**isIntersecting**: Boolean, true when element enters viewport

**intersectionRatio**: 0-1, percentage of element visible

## Common Pitfalls

**Multiple Observers**: Reuse observers for performance

**Disconnecting**: Always disconnect in cleanup

**CSS Timing**: Match transition duration with expected scroll speed

**Initial State**: Set opacity: 0 initially to avoid flash

## Task Protocol

When invoked:
1. Identify reveal type (fade, slide, scale)
2. Generate Intersection Observer setup
3. Include CSS transitions
4. Add React/Vue implementation if framework used
5. Optimize with once/disconnect patterns
6. Return complete implementation

## Related Droids

- `gsap-scrolltrigger` - More powerful scroll animations
- `locomotive-scroll` - Smooth scroll integration
- `motion-framer` - React animation framework
- `animated-component-libraries` - Component patterns
