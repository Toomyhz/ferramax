import api from "./axios";

const getCategories = async () => {
  const response = await api.get("/categories/");
  return response.data["CATEGORIAS"];
};

export default getCategories;
