package xyz.houtian17;

import org.bukkit.plugin.java.JavaPlugin;
import xyz.houtian17.playerevent.PlayerInteract;
import xyz.houtian17.playerevent.PlayerMove;
import xyz.houtian17.playerevent.WelcomeMessage;
import xyz.houtian17.command.CommandHello;
import xyz.houtian17.command.CommandSe;
import xyz.houtian17.command.CommandTps;

public class Plugin extends JavaPlugin {


    @Override
    public void onEnable() {
        getLogger().info("插件已被成功调用！");
        getServer().getPluginManager().registerEvents(new WelcomeMessage(), this);
        getServer().getPluginManager().registerEvents(new PlayerMove(), this);
        getServer().getPluginManager().registerEvents(new PlayerInteract(),this);
        getCommand("hello").setExecutor(new CommandHello());
        getCommand("tps").setExecutor(new CommandTps());
        getCommand("se").setExecutor(new CommandSe());
    }

    @Override
    public void onDisable() {

    }

}