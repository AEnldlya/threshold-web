# Image Optimization Pipeline

## WebP Conversion Script

```bash
#!/bin/bash
# scripts/convert-webp.sh

INPUT_DIR="${1:-.}"
OUTPUT_DIR="${2:-./optimized}"
QUALITY="${3:-80}"

mkdir -p "$OUTPUT_DIR"

for file in "$INPUT_DIR"/*.{jpg,jpeg,png,gif}; do
  [ -f "$file" ] || continue
  
  filename=$(basename "$file")
  filename_no_ext="${filename%.*}"
  
  # Convert to WebP
  cwebp "$file" -q "$QUALITY" -o "$OUTPUT_DIR/$filename_no_ext.webp"
  
  # Get file sizes
  original_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file")
  webp_size=$(stat -f%z "$OUTPUT_DIR/$filename_no_ext.webp" 2>/dev/null || stat -c%s "$OUTPUT_DIR/$filename_no_ext.webp")
  compression=$((100 - (webp_size * 100 / original_size)))
  
  echo "✓ $filename_no_ext.webp ($compression% smaller)"
done

echo "✓ All images converted to WebP"
```

## Responsive Image Generator

```tsx
// utils/responsive-images.ts
import sharp from 'sharp';
import path from 'path';
import fs from 'fs';

export async function generateResponsiveImages(imagePath: string) {
  const filename = path.parse(imagePath).name;
  const dir = path.dirname(imagePath);
  
  const sizes = [
    { width: 320, name: 'sm' },
    { width: 640, name: 'md' },
    { width: 1024, name: 'lg' },
    { width: 1280, name: 'xl' }
  ];

  const results = {
    webp: [],
    jpeg: []
  };

  for (const size of sizes) {
    // WebP format
    const webpPath = path.join(dir, `${filename}-${size.name}.webp`);
    await sharp(imagePath)
      .resize(size.width, null, { withoutEnlargement: true })
      .webp({ quality: 80 })
      .toFile(webpPath);
    
    results.webp.push(`${filename}-${size.name}.webp`);

    // JPEG fallback
    const jpegPath = path.join(dir, `${filename}-${size.name}.jpg`);
    await sharp(imagePath)
      .resize(size.width, null, { withoutEnlargement: true })
      .jpeg({ quality: 80, progressive: true })
      .toFile(jpegPath);
    
    results.jpeg.push(`${filename}-${size.name}.jpg`);
  }

  return results;
}

// Usage
export function ResponsiveImage({ src, alt, title }) {
  const filename = src.split('/').pop().split('.')[0];
  
  return (
    <picture>
      <source 
        srcSet={`
          /images/${filename}-sm.webp 320w,
          /images/${filename}-md.webp 640w,
          /images/${filename}-lg.webp 1024w,
          /images/${filename}-xl.webp 1280w
        `}
        type="image/webp"
      />
      <source 
        srcSet={`
          /images/${filename}-sm.jpg 320w,
          /images/${filename}-md.jpg 640w,
          /images/${filename}-lg.jpg 1024w,
          /images/${filename}-xl.jpg 1280w
        `}
        type="image/jpeg"
      />
      <img 
        src={src}
        alt={alt}
        title={title}
        loading="lazy"
        decoding="async"
      />
    </picture>
  );
}
```

## Blur-Up Placeholder Generator

```tsx
// utils/blur-placeholder.ts
import plaiceholder from 'plaiceholder';

export async function generateBlurPlaceholder(imagePath: string) {
  const { base64, img } = await plaiceholder(imagePath);
  
  return {
    blurDataUrl: base64,
    width: img.width,
    height: img.height,
    srcSet: `
      ${imagePath}?w=320&q=80 320w,
      ${imagePath}?w=640&q=80 640w,
      ${imagePath}?w=1024&q=80 1024w,
      ${imagePath}?w=1280&q=80 1280w
    `
  };
}

// Usage
export function ImageWithBlur({ src, alt }) {
  const [placeholder, setPlaceholder] = useState(null);

  useEffect(() => {
    generateBlurPlaceholder(src).then(setPlaceholder);
  }, [src]);

  if (!placeholder) return null;

  return (
    <img
      src={src}
      alt={alt}
      style={{
        backgroundImage: `url(${placeholder.blurDataUrl})`,
        backgroundSize: 'cover',
      }}
      onLoadingComplete={() => {
        // Remove blur once loaded
      }}
    />
  );
}
```

## Batch Processing Script

```tsx
// scripts/process-images.ts
import { spawn } from 'child_process';
import glob from 'glob';
import path from 'path';

export async function batchProcessImages(inputDir: string) {
  const images = glob.sync(`${inputDir}/**/*.{jpg,jpeg,png}`);
  
  const results = {
    processed: 0,
    failed: 0,
    totalSavings: 0
  };

  for (const imagePath of images) {
    try {
      const { webp, jpeg } = await generateResponsiveImages(imagePath);
      const { blurDataUrl } = await generateBlurPlaceholder(imagePath);
      
      // Calculate size savings
      // ... savings calculation
      
      results.processed++;
    } catch (error) {
      console.error(`Failed to process ${imagePath}:`, error);
      results.failed++;
    }
  }

  console.log(`✓ Processed ${results.processed} images`);
  console.log(`✗ Failed: ${results.failed}`);
  console.log(`📦 Total savings: ${(results.totalSavings / 1024 / 1024).toFixed(2)}MB`);

  return results;
}
```

## CDN Integration

```tsx
// config/cdn.ts
export const CDN_CONFIG = {
  provider: 'vercel', // or 'cloudflare'
  imageOptimization: {
    enabled: true,
    quality: 80,
    formats: ['webp', 'jpeg'],
    responsive: true
  }
};

// Usage with Next.js Image
import Image from 'next/image';

export function OptimizedImage({ src, alt, width, height }) {
  return (
    <Image
      src={src}
      alt={alt}
      width={width}
      height={height}
      sizes="(max-width: 640px) 100vw,
             (max-width: 1024px) 85vw,
             1200px"
      quality={80}
      priority={false}
      loading="lazy"
    />
  );
}
```

## Image Compression Monitoring

```tsx
// monitoring/image-metrics.ts
export async function checkImageSizes() {
  const images = document.querySelectorAll('img');
  const results = {
    totalSize: 0,
    optimization: {
      webp: 0,
      responsive: 0,
      lazy: 0
    }
  };

  images.forEach(img => {
    const isWebP = img.currentSrc?.includes('.webp');
    const hasResponsive = img.srcset !== '';
    const isLazy = img.loading === 'lazy';

    if (isWebP) results.optimization.webp++;
    if (hasResponsive) results.optimization.responsive++;
    if (isLazy) results.optimization.lazy++;
  });

  return results;
}
```

## Implementation Checklist

- [ ] WebP conversion script working
- [ ] Responsive image generator built
- [ ] Blur-up placeholders generated
- [ ] Batch processing script ready
- [ ] CDN integration configured
- [ ] Image compression monitoring
- [ ] Lazy loading implemented
- [ ] srcset generation automated
- [ ] Format fallbacks (WebP + JPEG)
- [ ] Performance metrics tracked
- [ ] Google Cloud Storage/Cloudinary integration
- [ ] Automated image optimization in CI/CD
