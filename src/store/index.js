import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    carrito: JSON.parse(localStorage.getItem("carrito")) || [],
  },
  mutations: {
    addToCart(state, producto) {
      const item = state.carrito.find(
        (item) => item.ID_HERRAMIENTA === producto.ID_HERRAMIENTA
      );
      if (!item) {
        state.carrito.push({ ...producto, cantidad: 1 });
      } else {
        item.cantidad++;
      }
      localStorage.setItem("carrito", JSON.stringify(state.carrito));
    },
    removeItemsByOne(state, productoId) {
      const item = state.carrito.find(
        (item) => item.ID_HERRAMIENTA === productoId
      );
      if (item && item.cantidad > 1) {
        item.cantidad--;
        localStorage.setItem("carrito", JSON.stringify(state.carrito));
      } else {
        state.carrito = state.carrito.filter(
          (item) => item.ID_HERRAMIENTA !== productoId
        );
      }
    },
    removeTotalFromCart(state, productoId) {
      state.carrito = state.carrito.filter(
        (item) => item.ID_HERRAMIENTA !== productoId
      );
      localStorage.setItem("carrito", JSON.stringify(state.carrito));
    },
    clearCart(state) {
      state.carrito = [];
      localStorage.setItem("carrito", JSON.stringify(state.carrito));
    },
  },
  actions: {
    agregarAlCarrito({ commit }, producto) {
      commit("addToCart", producto);
    },
    borrarItems({ commit }, productoId) {
      commit("removeItemsByOne", productoId);
    },
    removerDelCarrito({ commit }, productoId) {
      commit("removeTotalFromCart", productoId);
    },
    vaciarCarrito({ commit }) {
      commit("clearCart");
    },
    async iniciarPago({ getters }){
      const buyOrder = `O-${Date.now()}`;
      const sessionId = `S-${Date.now()}`;
      const amount = getters.totalCarrito;
      const returnUrl = 'http://localhost:5173/cart';
      try {
        await axios.post("http://localhost:5000/api/init_transaction/",{
          "amount" : amount,
          "buy_order" : buyOrder,
          "session_id" : sessionId,
          "return_url" : returnUrl
        },{
          headers: {
            'Content-Type':'application/json'
          }
        })
        .then(response =>{
          console.log(response.data['url']+'?token_ws='+response.data['token'])
          window.location.href = response.data['url']+'?token_ws='+response.data['token']
        })
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    }
  },
  getters: {
    carrito: (state) => state.carrito,
    totalCarrito: (state) => {
      const total = state.carrito.reduce((total, producto) =>{
        return total + producto.VALOR * producto.cantidad;
      }, 0);
      return total
    },
    formatearPrecio: () => (precio) => {
      return precio.toLocaleString('es-CL', { style: 'currency', currency:'CLP' })
    }
  },
});
