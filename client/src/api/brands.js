import api from "@/api/axios";

export const getBrands = async () => {
  const response = await api.get("/marcas/");
  return response.data["MARCAS"];
};

export const getBrandById = async (ID_MARCA) => {
  const response = await api.get(`/marcas/${ID_MARCA}`);
  return response.data[0];
};
