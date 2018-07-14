package xyz.houtian17.configfile;

import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;

public class playerJoin implements Listener {

    ConfigFile plugin;

    public playerJoin(ConfigFile instance) {
        plugin = instance;
    }

    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent e) {
        Player p = e.getPlayer();
        String playername = p.getName();
        if (!p.hasPlayedBefore()) {
            plugin.getConfig().set(playername + ".joined", 0);
            plugin.getConfig().set(playername + ".money", 0);
        }
        int joined = plugin.getConfig().getInt(playername + ".joined");
        plugin.getConfig().set(playername + ".joined", joined + 1);
        plugin.saveConfig();
    }
}