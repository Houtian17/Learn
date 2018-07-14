package xyz.houtian17.playerevent;

import org.bukkit.ChatColor;
import org.bukkit.Material;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.event.player.PlayerQuitEvent;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.PlayerInventory;

public final class WelcomeMessage implements Listener {
    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent e) {
        Player p = e.getPlayer();
        if (p.hasPlayedBefore()) {
            e.setJoinMessage(ChatColor.DARK_GREEN + "Welcome " + ChatColor.YELLOW + p.getName() + ChatColor.DARK_GREEN + " joined the game :)");
        } else {
            e.setJoinMessage(ChatColor.DARK_GREEN + "Welcome " + ChatColor.YELLOW + p.getName() + ChatColor.DARK_GREEN + " to my server :)");
        }
    }

    @EventHandler
    public void onPlayerQuit(PlayerQuitEvent e) {
        Player p = e.getPlayer();
        e.setQuitMessage(ChatColor.YELLOW + p.getName() + ChatColor.YELLOW + " has left the server :(");
    }
}
