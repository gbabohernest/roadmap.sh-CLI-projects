import process from "node:process";

/**
 * Get the movie category from the command line
 * @param category : string
 * @return string
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
  // console.log(movieCategories[category]);
};

const category = process.argv[2].trim();

if (!category) {
  console.log("Error, Please enter movie category to fetch details");
  process.exit(1);
}

getMovieCategory(category);
