library(ggplot2)
library(tidyr)
library(gridExtra)

# Cargar los datos
table <- read.table('/home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/Tablas_totales/configurational', header = TRUE)
data <- data.frame(
  table,
  res = factor(as.character(table$Res), levels = unique(as.character(table$Res)), ordered = TRUE),  
  vent = as.character(table$Ventana),  # Convertir Ventana a caracteres
  longmin = table$LongMin,
  longmax = table$LongHigh,
  longneu = table$LongNeu,
  wtmin = table$WTMin,
  wtmax = table$WTHigh,
  wtneu = table$WTNeu,
  shortmin = table$ShortMin,
  shortmax = table$ShortHigh,
  shortneu = table$ShortNeu
)

# Encontrar el valor máximo entre las tres variables
max_y <- max(max(data$longmin), max(data$longmax), max(data$longneu))

# Crear los gráficos con el mismo límite en el eje Y
plot_longmin <- ggplot(data, aes(x = res, y = table$LongMin, fill = vent)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~vent, scales = "free_y") +
  labs(title = "Long Minimally", x = "Residuo", y = "Cantidad") +
  scale_fill_brewer(palette = "Set1") +
  ylim(0, max_y)

plot_longmax <- ggplot(data, aes(x = res, y = table$LongHigh, fill = vent)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~vent, scales = "free_y") +
  labs(title = "Long Highly", x = "Residuo", y = "Cantidad") +
  scale_fill_brewer(palette = "Set1") +
  ylim(0, max_y)

plot_longneu <- ggplot(data, aes(x = res, y = table$LongNeu, fill = vent)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~vent, scales = "free_y") +
  labs(title = "Long Neutral", x = "Residuo", y = "Cantidad") +
  scale_fill_brewer(palette = "Set1") +
  ylim(0, max_y)

# Unir los gráficos en un solo subplot
grid.arrange(plot_longmin, plot_longmax, plot_longneu, ncol = 3)

max_y <- max(max(data$wtmin), max(data$wtmax), max(data$wtneu))

# Crear los gráficos con el mismo límite en el eje Y
plot_longmin <- ggplot(data, aes(x = res, y = table$WTMin, fill = vent)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~vent, scales = "free_y") +
  labs(title = "Water-mediated Minimally", x = "Residuo", y = "Cantidad") +
  scale_fill_brewer(palette = "Set1") +
  ylim(0, max_y)

plot_longmax <- ggplot(data, aes(x = res, y = table$WTHigh, fill = vent)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~vent, scales = "free_y") +
  labs(title = "Water-mediated  Highly", x = "Residuo", y = "Cantidad") +
  scale_fill_brewer(palette = "Set1") +
  ylim(0, max_y)

plot_longneu <- ggplot(data, aes(x = res, y = table$WTNeu, fill = vent)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~vent, scales = "free_y") +
  labs(title = "Water-mediated Neutral", x = "Residuo", y = "Cantidad") +
  scale_fill_brewer(palette = "Set1") +
  ylim(0, max_y)

# Unir los gráficos en un solo subplot
grid.arrange(plot_longmin, plot_longmax, plot_longneu, ncol = 3)

max_y <- max(max(data$shortmin), max(data$shortmax), max(data$shortneu))

# Crear los gráficos con el mismo límite en el eje Y
plot_longmin <- ggplot(data, aes(x = res, y = table$ShortMin, fill = vent)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~vent, scales = "free_y") +
  labs(title = "Short Minimally", x = "Residuo", y = "Cantidad") +
  scale_fill_brewer(palette = "Set1") +
  ylim(0, max_y)

plot_longmax <- ggplot(data, aes(x = res, y = table$ShortHigh, fill = vent)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~vent, scales = "free_y") +
  labs(title = "Short Highly", x = "Residuo", y = "Cantidad") +
  scale_fill_brewer(palette = "Set1") +
  ylim(0, max_y)

plot_longneu <- ggplot(data, aes(x = res, y = table$ShortNeu, fill = vent)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~vent, scales = "free_y") +
  labs(title = "Short Nuetral", x = "Residuo", y = "Cantidad") +
  scale_fill_brewer(palette = "Set1") +
  ylim(0, max_y)

# Unir los gráficos en un solo subplot
grid.arrange(plot_longmin, plot_longmax, plot_longneu, ncol = 3)

