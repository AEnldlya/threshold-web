import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "HapLink | Team 26532 - Happy Haptic Doctors",
  description: "FIRST Tech Challenge robotics team from Hanover, NH. Building competitive robots and innovative haptic technology.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="overflow-x-hidden">
        {children}
      </body>
    </html>
  );
}
