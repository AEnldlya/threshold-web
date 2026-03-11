// Form automation script for contacting businesses
// This script will be used to fill out contact forms on business websites

const businesses = [
  { name: "McNally Plumbing & Heating", email: "contact@mcnallyplumbing.com", likely_url: "mcnallyplumbing.com" },
  { name: "Salon Bella", email: "salelbella@gmail.com", likely_url: "salonbella-boston.com" },
  { name: "City Electric Services", email: "cityelectric@yahoo.com", likely_url: "cityelectric.com" },
  { name: "North End Pizzeria", email: "info@northendpizzeria.com", likely_url: "northendpizzeria.com" },
  { name: "Boston HVAC Solutions", email: "info@bostonhvacsolutions.com", likely_url: "bostonhvacsolutions.com" },
  { name: "Downtown Cleaning Services", email: "contact@downtownclean.com", likely_url: "downtowncleaningservices.com" },
  { name: "Perfect Paws Grooming", email: "perfectpaws.boston@gmail.com", likely_url: "perfectpawsgrooming.com" },
  { name: "Harbor Auto Repair", email: "harborauto@gmail.com", likely_url: "harborautorepair.com" },
  { name: "Urban Real Estate Group", email: "info@urbanrealty.boston", likely_url: "urbanrealty.boston" },
  { name: "Trinity Insurance Agency", email: "contact@trinityinsurance.com", likely_url: "trinityinsurance.com" },
  { name: "Sweet Creations Bakery", email: "sweetcreations.boston@gmail.com", likely_url: "sweetcreationsbakery.com" },
  { name: "Boston Landscaping & Design", email: "iabcd7@gmail.com", likely_url: "bostonlandscaping.com" },
  { name: "The Urban Gardener Landscape", email: "info@theurbangardenerlandscape.com", likely_url: "theurbangardenerlandscape.com" },
  { name: "Boston Contractors & Developers", email: "iabcd7@gmail.com", likely_url: "bostoncontractors.com" },
  { name: "Bright Dental Studio", email: "info@brightdental.boston", likely_url: "brightdental.boston" },
  { name: "Fitness First Gym", email: "contact@fitnessfirst.boston", likely_url: "fitnessfirst.boston" },
  { name: "Boston Tax & Accounting", email: "info@bostontaxaccounting.com", likely_url: "bostontaxaccounting.com" },
  { name: "Harbor View Restaurant", email: "reservations@harborview.boston", likely_url: "harborview.boston" },
  { name: "Quick Tax Solutions", email: "contact@quicktax.boston", likely_url: "quicktax.boston" },
  { name: "Eastern Electric Co", email: "info@easternelectric.boston", likely_url: "easternelectric.boston" },
  { name: "Premier Plumbing Boston", email: "service@premierplumbing.boston", likely_url: "premierplumbing.boston" },
  { name: "Chic Hair Salon", email: "chichairsalon@gmail.com", likely_url: "chichairsalon.com" },
  { name: "Italian Kitchen Restaurant", email: "info@italiankitchen.boston", likely_url: "italiankitchen.boston" },
  { name: "Professional HVAC Services", email: "info@professionalhvac.boston", likely_url: "professionalhvac.boston" },
  { name: "Green Clean Services", email: "contact@greenclean.boston", likely_url: "greenclean.boston" },
  { name: "Pooch Palace Grooming", email: "poochpalace.boston@gmail.com", likely_url: "poochpalacegrooming.com" },
  { name: "Reliable Auto Service", email: "reliableauto@gmail.com", likely_url: "reliableautoservice.com" },
  { name: "Boston Properties Realty", email: "info@bostonproperties.realty", likely_url: "bostonproperties.realty" },
  { name: "Guardian Insurance Partners", email: "contact@guardianinsurance.boston", likely_url: "guardianinsurance.boston" },
  { name: "Artisan Bakehouse", email: "artisan.bakehouse.boston@gmail.com", likely_url: "artisanbakehouse.com" }
];

const PITCH = "Hi there! We're a local Boston web design studio. We specialize in building professional websites for local businesses. Would you be interested in discussing a website redesign for your business? We typically build and deploy in 3-5 days. Let's chat!";

module.exports = { businesses, PITCH };
