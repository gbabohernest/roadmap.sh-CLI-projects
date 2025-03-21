import process from "node:process";
import { API_ACCESS_TOKEN } from "./apiKey.js";

/**
 * Get the movie category from the command line
 * @param category : string - The category of the movie
 * @return string - movie category (popular, now-playing, top-rated, upcoming)
 */
const getMovieCategory = (category) => {
  const movieCategories = {
    playing: "now_playing",
    popular: "popular",
    top: "top_rated",
    upcoming: "upcoming",
  };

  if (!(category in movieCategories)) {
    console.error("Error, Please provide a valid type");
    process.exit(1);
  }

  return movieCategories[category];
};

const fetchMovieDetails = async (movieCategory, accessToken) => {
  const url = `https://api.themoviedb.org/3/movie/${movieCategory}?language=en-US&page=1`;
  const header = {
    headers: {
      "User-Agent": "TMDB CLI Tools",
      Authorization: `Bearer ${accessToken}`,
    },
  };

  try {
    const response = await fetch(url, header);

    if (!response.ok) {
      throw new Error(
        `HTTP Error! Status: ${response.status} : Message: ${response.statusText}`,
      );
    }
    return await response.json();
  } catch (error) {
    console.error({ error: error.message });
  }
};

const displayMovieData = (movieData, movieCategory) => {
  const categories = {
    now_playing: "Now Playing",
    popular: "Popular",
    top_rated: "Top Rated",
    upcoming: "Upcoming",
  };

  const category_fields = {
    popular: ["title", "release_date", "popularity", "vote_count", "adult"],
    now_playing: ["title", "release_date", "adult"],
    top_rated: ["title", "release_date", "vote_average", "adult"],
    upcoming: ["title", "release_date", "adult"],
  };

  const field_headers = {
    title: "Movie Title",
    release_date: "Release Date",
    popularity: "Popularity",
    vote_count: "Vote Count",
    adult: "Adult Film",
    vote_average: "Rating",
  };
};

const category = process.argv[2].trim();

if (!category) {
  console.log("Error, Please enter movie category to fetch details");
  process.exit(1);
}

const movieCategory = getMovieCategory(category);
const data = await fetchMovieDetails(movieCategory, API_ACCESS_TOKEN);
console.log(data);
