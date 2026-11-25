# Hybrid redesign QA

Not yet browser-tested. Do not merge before approval.

- Preview this branch on a separate deployment (Vercel preview or local static server).
- Run Lighthouse mobile and desktop on PT and EN homepages; target performance >=90, LCP <=2.5s, CLS <=0.1, INP <=200ms (field metric).
- Compare against main using same device and throttling; repeat three times.
- Check widths 320, 375, 768, 1024, 1440px; no horizontal overflow.
- Verify navigation, language switching, project filters, project links, FAQ, email copy and sound toggle.
- Test keyboard navigation, focus, reduced motion, image loading and browser console.
- Check screenshot assets and fallback when images fail; no remote project iframe should load on hover.
- Review Safari and Chrome, including mobile touch.
- Confirm all project statuses and links with owner before merge.
