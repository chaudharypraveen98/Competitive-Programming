import { useEffect, useState } from "react";
import "./index.css";

const images = [
    {
        src: "https://picsum.photos/id/600/600/400",
        alt: "Forest",
    },
    {
        src: "https://picsum.photos/id/100/600/400",
        alt: "Beach",
    },
    {
        src: "https://picsum.photos/id/200/600/400",
        alt: "Yak",
    },
    {
        src: "https://picsum.photos/id/300/600/400",
        alt: "Hay",
    },
    {
        src: "https://picsum.photos/id/400/600/400",
        alt: "Plants",
    },
    {
        src: "https://picsum.photos/id/500/600/400",
        alt: "Building",
    },
];
function ImageCarouselContainer({
    images,
    options = {},
}: Readonly<{
    images: ReadonlyArray<{ src: string; alt: string }>;
    options?: { [key: string]: string };
}>) {
    const { speed = 200 } = options;
    const [currentIndex, setCurrentIndex] = useState(0);
    // useEffect(() => {
    //     const interval = setInterval(() => {
    //         setCurrentIndex((prev) => (prev >= images?.length ? 0 : prev + 1));
    //     }, speed);

    //     return () => {
    //         clearInterval(interval);
    //     };
    // }, []);
    const handleNext = () => {
        setCurrentIndex((prev) => (prev >= images?.length - 1 ? 0 : prev + 1));
    };
    const handlePrev = () => {
        setCurrentIndex((prev) => (prev === 0 ? images.length - 1 : prev - 1));
    };
    return (
        <div className="imageCarousel__container">
            {/* {images.map(({ alt, src }) => (
                <div className="imageCarousel__slide">
                    <img key={src} alt={alt} src={src} width="100%" />
                </div>
            ))} */}
            <div className="imageCarousel__slide">
                <img
                    key={images[currentIndex].src}
                    alt={images[currentIndex].alt}
                    src={images[currentIndex].src}
                    width="100%"
                />
            </div>

            <button
                type="button"
                className=" imageCarousel__btn imageCarousel__btn_left"
                onClick={handlePrev}
            >
                {"<"}
            </button>
            <button
                type="button"
                className="imageCarousel__btn imageCarousel__btn_right"
                onClick={handleNext}
            >
                {">"}
            </button>
            <div className="imageCarousel__dots">
                {images?.map((_, index) => (
                    <div
                        className={`imageCarousel__dot ${index === currentIndex ? "imageCarousel__dot_active" : ""}`}
                    ></div>
                ))}
            </div>
        </div>
    );
}

export default function ImageCarousel() {
    return (
        <div className="flex justify-center bg-black">
            <ImageCarouselContainer images={images} />
        </div>
    );
}
